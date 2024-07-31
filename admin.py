from django.contrib import admin

# Register your models here.
from .models import Post, Category

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass