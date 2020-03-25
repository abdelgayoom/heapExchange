from django.urls import path
from . import views

urlpatterns = [

    path('post', views.posts_list),
    path('post/<int:pk>', views.posts_detail),
]