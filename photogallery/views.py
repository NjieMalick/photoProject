from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .forms import PostForm
from .models import Post


class HomeView(ListView):
	model = Post
	template_name = 'photogallery/home.html'


class CreatePostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'photogallery/create_post.html'
	success_url = reverse_lazy('home')

