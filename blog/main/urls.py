from django.urls import path
from . import views
from . views import HomeView, ArticleDetail, AddPostView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetail.as_view(), name='article-detail'),
    path('add-post', AddPostView.as_view(), name='add-post')
]
