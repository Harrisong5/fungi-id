from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import User, Profile, Fungi, Safety, CommunityPost

class PostList(generic.ListView):
    model = CommunityPost
