from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
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
        context['GOOGLE_MAPS_API_KEY'] = settings.GOOGLE_MAPS_API_KEY
        context['posts'] = CommunityPost.objects.filter(status=1)
        return context

class PostsList(generic.ListView):
    queryset = CommunityPost.objects.filter(status=2)
    template_name = "id/posts.html"
    context_object_name = 'post_list'

class ProfilePage(LoginRequiredMixin, ListView):
    model = CommunityPost
    template_name = "id/profile.html"
    context_object_name = 'posts'

    def get_queryset(self):
        # Get the current user
        current_user = self.request.user
        # Return only the posts of the current user
        return CommunityPost.objects.filter(user_id=current_user).order_by('-time')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        # Add user details to the context
        context['user_details'] = {
            'username': current_user.username,
            'email': current_user.email,
            'password': current_user.password,
            'date_joined': current_user.date_joined
            # Add more fields as needed
        }
        profile = Profile.objects.get(user=current_user)

        context['profile_details'] = {
            'image_url': profile.image_url.url if profile.image_url else None,
            'bio': profile.bio,
            'created_on': profile.created_on,
            'last_updated': profile.last_updated,
        }
        
        return context
