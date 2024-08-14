from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile_user")
    image_url = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    bio = models.TextField(max_length=1000, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

class Fungi(models.Model):
    fungi_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=255, unique=True)
    genus = models.CharField(max_length=255)
    family = models.CharField(max_length=255)
    description = models.TextField()
    habitat = models.CharField(max_length=255)
    image_url = models.ImageField(upload_to='fungi_images/', null=True, blank=True)
    lookalikes = models.CharField(max_length=255)

    TOXICITY_CHOICES = (
        (6, 'Fatal'),
        (5, 'Harmful'),
        (4, 'Edible'),
        (3, 'Psychoactive'),
        (2, 'Medicinal'),
        (1, 'Cullinary'),
        (0, 'Unknown'),
    )
    toxicity = models.IntegerField(choices=TOXICITY_CHOICES, default=0)


    def __str__(self):
        return f"{self.name} ({self.species})"

class Identified(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fungi_id = models.ForeignKey(Fungi, on_delete=models.SET_NULL, null=True, blank=True)
    image_url = models.ImageField(upload_to='identified_images/')
    location = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
