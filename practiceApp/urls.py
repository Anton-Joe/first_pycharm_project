from django.urls import path
from practiceApp import  views

app_name = 'practiceApp'

urlpatterns = [
    path('', views.index, name='test_name'),
    path('/room2/<room_id>', views.room_id),
    path('/room/', views.room_id2)
]