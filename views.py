from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from djangoProject.blog.models import Post, Category
from .forms import PostForm, EditForm

# class-based view
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    categories_types = Category.objects.all()
    ordering = ['-created']

    def get_context_data(self, *args,**kwargs):
        category_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args,**kwargs)
        context['category_menu'] = category_menu
        return context

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context['category_menu'] = category_menu
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    # fields = ['title', 'title_tag', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class AddCategoryView(CreateView):
    model = Category
    fields = '__all__'
    template_name = 'add_category.html'



# function-based view
def CategoryView(request, categories_types):
    formatted_category = categories_types.replace('-', ' ')
    category_post = Post.objects.filter(category__iexact=formatted_category)

    # Debugging statement
    # print(f"Formatted Category: {formatted_category}, Post Count: {category_post.count()}")

    context = {'categories_types': formatted_category, 'category_post': category_post}
    return render(request, 'categories.html', context)

    # category_post = Post.objects.filter(category=categories_types.replace('-', ' '))
    # context = {'categories_types': categories_types.replace('-', ' '),'category_post': category_post}
    # return render(request, 'categories.html', context)