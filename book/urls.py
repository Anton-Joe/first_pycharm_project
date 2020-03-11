from django.urls import path
from book import  views

urlpatterns = [
    path('', views.book),
    path('/detail/<book_id>/<category_id>', views.book_detail),
    path('/book_list', views.book_list)
]