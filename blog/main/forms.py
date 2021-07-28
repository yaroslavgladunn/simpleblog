from django import forms
from . models import Post, Category

choices = Category.objects.all().values_list('name', 'name')

choice_list = []
for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
	class Meta:
	   model = Post
	   fields = ('title', 'title_tag', 'author', 'category', 'header_image', 'body',)

	   widgets = {
		  'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name your article'}),
		  'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Short description'}),
		  'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user', 'type': 'hidden'}),
		  'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
		  'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Hello..'}),

	   }


class EditForm(forms.ModelForm):
	class Meta:
	   model = Post
	   fields = ('title', 'title_tag', 'category', 'header_image', 'body')

	   widgets = {
		  'title': forms.TextInput(attrs={'class': 'form-control'}),
		  'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
		   'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
		  'body': forms.Textarea(attrs={'class': 'form-control'}),
	   }




