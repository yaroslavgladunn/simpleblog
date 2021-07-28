from django.urls import path
from .views import UserRegister, UserEditView, PasswordsChangeView, password_success, ProfilePageView, EditProfilePageView, CreateProfilePage
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
	path('register/', UserRegister.as_view(), name='register'),
	path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
	path('password/', PasswordsChangeView.as_view(template_name='registration/change_password.html')),
    	path('password_success/', views.password_success, name='password_success'),
    	path('<int:pk>/profile/', ProfilePageView.as_view(), name='profile_page'),
	path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),
    	path('create_profile_page/', CreateProfilePage.as_view(), name='create_profile_page'),

]
