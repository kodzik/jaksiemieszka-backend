from django.db import models

# Create your models here.
class User(models.Model):

    id = models.CharField(primary_key=True, max_length=100)
    email = models.EmailField(max_length=100)
    # role =
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    token = models.CharField(max_length=100) # UWAGA NA DLUGOSC!!!!!!!

    def __str__(self):
        return self.id
