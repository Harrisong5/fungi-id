from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic import TemplateView
from .models import User, Profile, Fungi, Safety, CommunityPost

class PostList(generic.ListView):
    queryset = CommunityPost.objects.filter(status=2)
    template_name = "id/index.html"
    context_object_name = 'post_list'

class MapView(generic.ListView):
    queryset = CommunityPost.objects.filter(status=2)
    template_name = "id/map.html"
    context_object_name = 'post_list'

class PostsList(generic.ListView):
    queryset = CommunityPost.objects.filter(status=2)
    template_name = "id/posts.html"
    context_object_name = 'post_list'