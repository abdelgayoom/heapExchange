from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [

    path('', views.PostListView.as_view(), name='home'),
    path('user_post/<str:username>/', views.UserPostListView.as_view(), name='user_posts'),
   # path('post/<int:pk>/add_comment/', views.comment_view, name='new_comment'),
    path('post/<int:pk>/', views.comment_view, name='detail'),
    path('post/new/', views.PostCreateView.as_view(), name='create'),
    path('post/<int:pk>/update', views.PostUpdateView.as_view(), name='update'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='delete'),
    path('contact/', views.ContactView.as_view(), name='contact'),

]
