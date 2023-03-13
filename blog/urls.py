from django.urls import path 
from .views import *

urlpatterns = [
	path('', HomeView.as_view(), name='home'),
	path("article/<int:pk>", ArticleDetail.as_view(), name="article_details"),
	path("addpost/", AddPostView.as_view(), name="add_post"),
	path("addcatagory/", AddCatagoryView.as_view(), name="addcatagory"),
	path("article/edit/<int:pk>", UpdatePostView.as_view(), name="edit_post"),
	path("article/<int:pk>/remove", DeletePostView.as_view(), name="delete_post"),
	path("catagory/<str:cats>/", catagoryView, name="catagory"),
]