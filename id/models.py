from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile_user")
    image_url = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    bio = models.TextField(max_length=1000, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)


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



class Safety(models.Model):

    fungi_id = models.ForeignKey(Fungi, on_delete=models.CASCADE)
   
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
    precautions = models.TextField()
    symptoms = models.TextField()
    first_aid = models.TextField()

class CommunityPost(models.Model):
    post_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    fungi_id = models.ForeignKey(Fungi, on_delete=models.CASCADE)
    image_url = models.ImageField(upload_to='media/community_images/')
    location = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=12, decimal_places=8, default=None, blank=True, null=True)
    longitude = models.DecimalField(max_digits=12, decimal_places=8, default=None, blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    STATUS = (
        (0, 'Pending'),
        (1, 'Public'),
        (2, 'Private'),
        (3, 'Rejected'),

    )

    status = models.IntegerField(choices=STATUS, default=0)

class Identified(models.Model):

    list_name = models.CharField(max_length=255, default='unnamed list')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ManyToManyField(CommunityPost)
