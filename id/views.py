from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import User, Profile, Fungi, Safety, CommunityPost

class PostList(generic.ListView):
    queryset = CommunityPost.objects.filter(status=2)
    template_name = "id/index.html"
    context_object_name = 'post_list'