from django.urls import path
from . import views

urlpatterns = [
    path('', views.QuestionsListView.as_view(), name='question_list'),


]