from django import forms
from .models import *

choice =  [ i for i in Catagory.objects.all().values_list('name','name')]

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = '__all__'

		widgets = {
			'title' : forms.TextInput(attrs={'class' :'form-control'}),
			'author' : forms.Select(attrs={'class' :'form-control'}),
			'catagory' : forms.Select(choices=choice,attrs={'class' :'form-control'}),
			'body' : forms.Textarea(attrs={'class' :'form-control'}),
		}

class CatagoryForm(forms.ModelForm):
	class Meta:
		model = Catagory
		fields = '__all__'
		widgets = {
			'catagory' : forms.TextInput(attrs={'class' :'form-control'}),
		}

class EditForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','catagory','body')

		widgets = {
			'title' : forms.TextInput(attrs={'class' :'form-control'}),
			'catagory' : forms.Select(choices=choice,attrs={'class' :'form-control'}),
			'body' : forms.Textarea(attrs={'class' :'form-control'}),
		}