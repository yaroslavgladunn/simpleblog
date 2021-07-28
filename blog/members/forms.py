from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from main.models import Profile

class ProfilePageForm(forms.ModelForm):
    class Meta:
       model = Profile
       fields = ('bio', 'country', 'profile_pic', 'website_url', 'facebook_url', 'instagram_url', 'twitter_url', 'pinterest_url')

    widgets = {
       'country': forms.TextInput(attrs={'class': 'form-control'}),
        'profile_pic': forms.ImageField(),
       'bio': forms.Textarea(attrs={'class': 'form-control'}),
       'website_url': forms.TextInput(attrs={'class': 'form-control'}),
       'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),
       'instagram_url': forms.TextInput(attrs={"class": 'form-control'}),
       'twitter_url': forms.TextInput(attrs={'class': 'form-control'}),
       'pinterest_url': forms.TextInput(attrs={'class': 'form-control'}),
    }


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
       model = User
       fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

       widgets = {
          'first_name': forms.TextInput(attrs={'class': 'form-control'}),
          'last_name': forms.TextInput(attrs={'class': 'form-control'}),
          'username': forms.TextInput(attrs={'class': 'form-control'}),
          'email': forms.EmailInput(attrs={'class': 'form-control'}),
          'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
          'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
       }

class UpdateProfileForm(UserChangeForm):
    class Meta:
       model = User
       fields = ('username', 'email', 'first_name', 'last_name', )

       widgets = {
          'username': forms.TextInput(attrs={'class': 'form-control'}),
          'email': forms.EmailInput(attrs={'class': 'form-control'}),
          'first_name': forms.TextInput(attrs={'class': 'form-control'}),
          'last_name': forms.TextInput(attrs={'class': 'form-control'}),

       }

class PasswordChangingForm(PasswordChangeForm):
    class Meta:
       model = User
       fields = ('old_password', 'new_password1', 'new_password2')

       widgets = {
          'old_password': forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}),
          'new_password1': forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}),
          'new_password2': forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}),
       }
