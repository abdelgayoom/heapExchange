from django.urls import path
from . import views

app_name = 'questions'

urlpatterns = [
    path('', views.QuestionsListView.as_view(), name='question_list'),
    path('<int:pk>', views.question_view, name='detail'),
    path('new', views.QuestionCreateView.as_view(), name='new_question'),
    path('<int:pk>/update', views.QuestionUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', views.QuestionDeleteView.as_view(), name='delete'),
    path('answer/<int:pk>/update', views.AnswerUpdateView.as_view(), name='update_answer'),
    path('answer/<int:pk>/delete', views.AnswerDeleteView.as_view(), name='delete_answer'),
]