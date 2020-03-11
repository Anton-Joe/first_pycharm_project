"""first_pycharm_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from book import views
from movie.views import movie
from django.urls import converters

def index(request):
    return HttpResponse('首页')


urlpatterns = [
    path('admin/', admin.site.urls),
    # http://127.0.0.1:8000
    path('', index),
    # http://127.0.0.1:8000/book/
    # path('book/', views.book),
    # http://127.0.0.1:8000/movie
    path('movie/', movie),
    # http://127.0.0.1:8000/book/
    # path('book/detail/<book_id>/<category_id>', views.book_detail),
    # path('book/author/', views.author_detail),
    # path('book/publisher/<int:publisher_id>', views.publisher_detail)

    path('front', include('front.urls')),

    path('book', include('book.urls'))
]
