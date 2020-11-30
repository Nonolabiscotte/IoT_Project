from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('home/<int:code_id>/', views.room_list, name='room_list'),
    path('home/graphics', views.graphic_generator, name='graphic_generator'),
]
