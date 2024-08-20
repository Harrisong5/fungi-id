from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('map', views.MapView.as_view(), name='map'),
    path('posts', views.PostsList.as_view(), name='posts'),
    path('new_sighting', views.PostsList.as_view(), name='new_sighting'),
]