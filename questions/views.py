from django.shortcuts import render, get_object_or_404, redirect
from .models import Questions, Answers
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .forms import AnswersCreationForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class QuestionsListView(ListView):
    model = Questions
    template_name = 'questions/questions_list.html'
    context_object_name = 'question'
    paginate_by = 5
    ordering = ['-date_asked']


# question detail view and answers list view
def question_view(request, pk):
    question = get_object_or_404(Questions, pk=pk)
    if request.method == 'POST':
        form = AnswersCreationForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.questions = question
            answer.save()
            messages.success(request, f'your answer had been created')
            return redirect('questions:detail', pk=question.pk)
    else:
        form = AnswersCreationForm()
        question = get_object_or_404(Questions, pk=pk)
    return render(request, 'questions/question_detail.html', {'form': form, 'question': question})


# question create view
class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Questions
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class QuestionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Questions
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.author:
            return True
        return False


class QuestionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Questions
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class AnswerUpdateView(UpdateView):
    model = Answers
    template_name = 'questions/answer_update.html'
    fields = ['body']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        answer = self.get_object()
        if self.request.user == answer.user:
            return True
        return False


# comment delete view
class AnswerDeleteView(DeleteView):
    model = Answers
    success_url = '/'

    def test_func(self):
        answer = self.get_object()
        if self.request.user == answer.user:
            return True
        return False




