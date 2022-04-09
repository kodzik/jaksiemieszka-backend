import string
import uuid
from django.db import models
from django.contrib.auth.models import User

class CommentRating(models.Model):
    # id = models.IntegerField(primary_key=True, editable=False)
    location = models.IntegerField()
    air = models.IntegerField()
    noise = models.IntegerField()
    traffic = models.IntegerField()

class Address(models.Model):
    road = models.CharField(max_length=100, blank=True, null=True)
    house_number = models.CharField(max_length=100, blank=True, null=True)
    suburb = models.CharField(max_length=100, blank=True, null=True)
    neighbourhood = models.CharField(max_length=100, blank=True, null=True)
    quarter = models.CharField(max_length=100, blank=True, null=True)

class Comment(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    when_added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    location_lat = models.FloatField()
    location_lng = models.FloatField()
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)
    rating = models.ForeignKey(CommentRating, on_delete=models.CASCADE)
    text_content = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.id)

