from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

# Create your views here.
#def home(request):
#    return render(request, 'main/home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'main/home.html'

class ArticleDetail(DetailView):
    model = Post
    template_name = 'main/article_detail.html'

class AddPostView(CreateView):
    model = Post
    template_name = 'main/add_post.html'
    fields = '__all__'
