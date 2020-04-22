from django.urls import path

from .views import HomeView, CreatePostView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/', CreatePostView.as_view(), name='add_post'),
]
