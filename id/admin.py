from django.contrib import admin
from .models import Profile, Fungi, Identified, Safety, CommunityPost

# Register your models here.
admin.site.register(Profile)
admin.site.register(Fungi)
admin.site.register(Identified)
admin.site.register(Safety)
admin.site.register(CommunityPost)