from rest_framework import serializers
from .models import Address, CommentRating, Comment
from django.contrib.auth.models import User


class AddressSerializer(serializers.ModelSerializer):

    def to_internal_value(self, data):
        return {
            'road': data['road'], 
            'house_number': data['house_number'], 
            'suburb': data['suburb'], 
            'neighbourhood': data['neighbourhood'],
            'quarter': data['quarter']
        }

    class Meta:
        model = Address
        fields = ('__all__')

class RatingSerializer(serializers.ModelSerializer):

    def to_internal_value(self, data):
        return {
            'location': data['location'], 
            'air': data['air'], 
            'noise': data['noise'], 
            'traffic': data['traffic']}

    class Meta:
        model = CommentRating
        exclude = ('id', )
         

class LocationSerializer(serializers.Field):

    def to_representation(self, location):
        return {'lat': location.location_lat, 'lng': location.location_lng}

    def to_internal_value(self, data):
        return {"location_lat": data['lat'], "location_lng": data['lng']}


class CommentSerializer(serializers.ModelSerializer):#changed from HyperlinkedModelSerializer

    id = serializers.UUIDField(read_only=True)
    username = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username') #read_only=True
    when_added = serializers.DateTimeField(read_only=True)

    location = LocationSerializer( source='*')#
    rating = RatingSerializer()
    address = AddressSerializer()
    # text_content = serializers.CharField()

    class Meta:
        model = Comment
        fields = ('id', 'username', 'location', 'rating', 'when_added', 'last_modified', 'text_content', 'address')

    def create(self, validated_data):
        username=validated_data.pop('username')
        username = User.objects.get(username=username) #User.objects.first() #TODO get active user username  #
        rating_data = validated_data.pop('rating')
        address_data = validated_data.pop('address')
        rating = CommentRating.objects.create(**rating_data)
        address = Address.objects.create(**address_data)
        comment = Comment.objects.create(username=username, rating=rating, address=address, **validated_data)
        return comment