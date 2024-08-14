from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile_user")
    username = models.CharField(max_length=32, unique=True)
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

    TOXICITY_CHOICES = [
        ('fatal', 'Fatal'),
        ('harmful', 'Harmful'),
        ('medicinal', 'Medicinal'),
        ('cullinary', 'Cullinary'),
        ('psychoactive', 'Psychoactive'),
        ('edible', 'Edible'),
        ('unknown', 'Unknown'),
    ]
    toxicity = models.CharField(max_length=12, choices=TOXICITY_CHOICES, default='unknown')


    def __str__(self):
        return f"{self.name} ({self.species})"