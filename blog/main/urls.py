from django.urls import path
# from . import views
from . views import HomeView, ArticleDetail, AddPostView, EditPost, DeletePost

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetail.as_view(), name='article-detail'),
    path('add-post', AddPostView.as_view(), name='add-post'),
    path('article/edit/<int:pk>', EditPost.as_view(), name='edit_post'),
    path('article/<int:pk>/delete-post', DeletePost.as_view(), name='delete_post')
]
