from django.shortcuts import render
from .models import Questions, Answers
from django.views.generic import ListView, DetailView, UpdateView, DeleteView


class QuestionsListView(ListView):
    model = Questions
    template_name = 'questions/questions_list.html'
    context_object_name = 'question'
    paginate_by = 5
    ordering = ['-date_asked']








