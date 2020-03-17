from django.urls import path
from cms import  views
app_name = 'CMS'

urlpatterns = [
    path('', views.index, name='index'),
    path('/login', views.login, name='login')
]