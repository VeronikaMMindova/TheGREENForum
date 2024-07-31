
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('djangoProject.blog.urls')),
    path('members/', include('django.contrib.auth.urls')), #login is one of them urls
    path('members/', include('djangoProject.members.urls')),
]