from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . models import Post
from . forms import PostForm, EditForm
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Post
    template_name = 'main/home.html'
    ordering = ['-id']

class ArticleDetail(DetailView):
    model = Post
    template_name = 'main/article_detail.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'main/add_post.html'

class EditPost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'main/update_post.html'

class DeletePost(DeleteView):
    model = Post
    template_name = 'main/delete_post.html'
    success_url = reverse_lazy('home')




