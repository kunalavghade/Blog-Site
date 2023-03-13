from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
from .forms import *
# Create your views here.

class HomeView(ListView):
	model = Post
	template_name = 'home.html'


def catagoryView(request, cats):
	print(cats)
	catagory_post = Post.objects.filter(catagory = cats)
	return  render(request, 'catagorys.html', {'cats':cats, 'catagory_post': catagory_post })

class ArticleDetail(DetailView):
	model = Post
	template_name = 'article_details.html'

class AddPostView(CreateView):
	model = Post
	form_class =  PostForm
	template_name = 'add_post.html'
	success_url = reverse_lazy('home')

class AddCatagoryView(CreateView):
	model = Catagory
	form_class = CatagoryForm
	template_name = 'add_catagory.html'

class UpdatePostView(UpdateView):
	model = Post
	form_class =  EditForm
	template_name = 'edit.html'

class DeletePostView(DeleteView):
	model = Post
	template_name = 'delete_post.html'
	success_url = reverse_lazy('home')