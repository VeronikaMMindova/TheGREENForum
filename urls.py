from django.urls import path
from . import views
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, \
    CategoryView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/details/<int:pk>/', ArticleDetailView.as_view(), name='article_details'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>/', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/delete/', DeletePostView.as_view(), name='delete_post'),
    path('add-category/', AddCategoryView.as_view(), name='add_category'),
    path('category/<str:categories_types>/', CategoryView, name='category'),
]