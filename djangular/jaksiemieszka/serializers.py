from rest_framework import serializers
from .models import CommentRating, Comment
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('__all__')

class RatingSerializer(serializers.ModelSerializer):
    location = serializers.IntegerField()
    air = serializers.IntegerField()
    noise = serializers.IntegerField()
    traffic = serializers.IntegerField()

    # def get_rating(self, obj):
    #     # return '{} {}'.format(obj.location, obj.air, obj.noise, obj.traffic) 
    #     return { "location": obj.location, "air": obj.air, "noise": obj.noise, "traffic": obj.traffic}

    class Meta:
        model = CommentRating
        exclude = ('id', )
         

class LocationSerializer(serializers.Field):
    # def to_internal_value(self, location):
    #     return location.location_lat, location.location_lng

    def to_representation(self, location):
        return {'lat': location.location_lat, 'lng': location.location_lng}

class CommentSerializer(serializers.ModelSerializer):

    id = serializers.UUIDField(read_only=True)
    username = serializers.SlugRelatedField(read_only=True, slug_field='username')
    when_added = serializers.DateTimeField(read_only=True)

    location = LocationSerializer(source='*')#
    rating = RatingSerializer()

    # def get_dupa(self, obj):
    #     return '{} {}'.format(obj.location_lat, obj.location_lng) 

    class Meta:
        model = Comment
        fields = ('id', 'username', 'location', 'rating', 'when_added', 'last_modified')#,, 
        # fields = ('__all__')    
