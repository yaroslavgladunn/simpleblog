from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . forms import PostForm, EditForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from . models import Post, Category
from django.http import HttpResponseRedirect


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))



class HomeView(ListView):
    model = Post
    template_name = 'main/home.html'
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data()
        context['cat_menu'] = cat_menu
        return context


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'main/categories.html', {'cats': cats.title(), 'category_posts': category_posts})


class ArticleDetail(DetailView):
    model = Post
    template_name = 'main/article_detail.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetail, self).get_context_data()

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['cat_menu'] = cat_menu
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context

class AddPostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'main/add_post.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddPostView, self).get_context_data()
        context['cat_menu'] = cat_menu
        return context



class EditPost(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'main/update_post.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(EditPost, self).get_context_data()
        context['cat_menu'] = cat_menu
        return context

class DeletePost(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'main/delete_post.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(DeletePost, self).get_context_data()
        context['cat_menu'] = cat_menu
        return context

# class CategoryView(LoginRequiredMixin, CreateView):
#     model = Category
#     template_name = 'main/category.html'





