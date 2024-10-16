from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('map/', views.MapView.as_view(), name='map'),
    path('posts', views.PostsList.as_view(), name='posts'),
    path('new_sighting', views.PostsList.as_view(), name='new_sighting'),
    path('profile', views.ProfilePage.as_view(), name='profile'),
    path('lists', views.IdentifiedCreateView.as_view(), name='lists'),
   
    
    
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

