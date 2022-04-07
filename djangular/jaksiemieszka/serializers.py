from rest_framework import serializers
from .models import CommentRating, Comment
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True, max_length=100)

    class Meta:
        model = User
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


class CommentSerializer(serializers.ModelSerializer):

    id = serializers.UUIDField(read_only=True)
    username = serializers.SlugRelatedField(read_only=True, slug_field='username')
    when_added = serializers.DateTimeField(read_only=True)

    location = LocationSerializer( source='*')#
    rating = RatingSerializer()
    # text_content = serializers.CharField()

    class Meta:
        model = Comment
        fields = ('id', 'username', 'location', 'rating', 'when_added', 'last_modified', 'text_content')

    def create(self, validated_data):
        username = User.objects.first() #TODO get active user username
        rating_data = validated_data.pop('rating')
        rating = CommentRating.objects.create(**rating_data)
        comment = Comment.objects.create(username=username, rating=rating, **validated_data)
        return comment