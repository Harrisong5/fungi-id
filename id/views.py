from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic import TemplateView
from .models import User, Profile, Fungi, Safety, CommunityPost
from django.conf import settings

class PostList(generic.ListView):
    queryset = CommunityPost.objects.filter(status=2)
    template_name = "id/index.html"
    context_object_name = 'post_list'

class MapView(TemplateView):
    template_name = "id/map.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['GOOGLE_MAPS_API_KEY'] = settings.GOOGLE_MAPS_API_KEY  # Add your API key to the context
        return context

class PostsList(generic.ListView):
    queryset = CommunityPost.objects.filter(status=2)
    template_name = "id/posts.html"
    context_object_name = 'post_list'

