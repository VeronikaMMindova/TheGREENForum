from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    title = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )
    title_tag = models.CharField(
        max_length=100,
        default="Let's plant"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    created = models.DateTimeField(
        auto_now_add=True,
    )
    category = models.CharField(
        max_length=100,
        default='Flower',
    )


    def __str__(self):
        return f'"{self.title}" by   -{str(self.author)}- at:  {self.created}'



    def get_absolute_url(self):
        # return reverse('article_details', args=(str(self.id)))
        return reverse('home')
