from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic, View
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User, Profile, Fungi, Safety, CommunityPost, Identified
from .forms import CommunityPostForm, IdentifiedForm
from django.conf import settings
from django.utils.decorators import method_decorator

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
         # Check if the profile exists, and create one if it doesn't
        profile, created = Profile.objects.get_or_create(user=current_user)

        # Add profile details to the context
        context['profile_details'] = {
            'image_url': profile.image_url.url if profile.image_url else None,
            'bio': profile.bio,
            'created_on': profile.created_on,
            'last_updated': profile.last_updated,
        }



        context['profile_details'] = {
            'image_url': profile.image_url.url if profile.image_url else None,
            'bio': profile.bio,
            'created_on': profile.created_on,
            'last_updated': profile.last_updated,
        }
        
        identified_lists = Identified.objects.filter(user=current_user)
        context['identified_lists'] = identified_lists
        
        return context


class CommunityPostCreateView(LoginRequiredMixin, ListView):
    def get(self, request):
        form = CommunityPostForm()
        return render(request, 'id/create_community_post.html', {'form': form})

    def post(self, request):
        form = CommunityPostForm(request.POST, request.FILES)
        if form.is_valid():
            community_post = form.save(commit=False)
            community_post.user_id = request.user  # Link the post to the current user
            community_post.save()
            return redirect('community_post_success')  # Redirect after successful post creation

        return render(request, 'id/create_community_post.html', {'form': form})

class IdentifiedCreateView(View):
    def get(self, request):
        form = IdentifiedForm(user=request.user)  # Pass the logged-in user
        return render(request, 'id/identified.html', {'form': form})

    def post(self, request):
        form = IdentifiedForm(request.POST, user=request.user)  # Pass the logged-in user
        if form.is_valid():
            identified = form.save(commit=False)
            identified.user = request.user  # Associate the logged-in user
            identified.save()
            # Save the many-to-many relationship for post_id
            form.save_m2m()
            return redirect('profile')  # Redirect to a success page
        return render(request, 'id/identified.html', {'form': form})