
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Posts, Comments
from .forms import ContactForm, CommentsCreationForm
from django.views import View
from django.core.mail import send_mail
from lisa.settings import SecretData


class PostListView(ListView):
    model = Posts
    template_name = 'blog/home.html'
    context_object_name = 'post'
    paginate_by = 5
    ordering = ['-date_post']


class UserPostListView(ListView):
    model = Posts
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Posts.objects.filter(author=user).order_by('-date_post')


#def post_detail(request, pk):
  #  post = get_object_or_404(Posts, pk=pk)
   # return render(request, 'blog/posts_detail.html', {'post': post})


#class PostDetailView(DetailView):
  #  model = Posts
   # template_name = 'blog/posts_detail.html'
  #  context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Posts
    fields = ['title', 'subject']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Posts
    fields = ['title', 'subject']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Posts
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# comments views

def comment_view(request, pk):
    posts = get_object_or_404(Posts, pk=pk)
    if request.method == 'POST':
        form = CommentsCreationForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.posts = posts
            comment.save()
            return redirect('blog:detail', pk=posts.pk)
    else:
        form = CommentsCreationForm()
        post = get_object_or_404(Posts, pk=pk)
    return render(request, 'blog/posts_detail.html', {'form': form, 'post': post})







# contact form for sending email
class ContactView(View):
    def post(self, request):
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                subject = form.cleaned_data['subject']
                message = form.cleaned_data['message']
                email = form.cleaned_data['email']
                recipients = list()
                recipients.append(SecretData.get('EMAIL_HOST_USER'))
                send_mail(subject, message, email, recipients)
                return redirect('blog:home')

    def get(self, request):
        form = ContactForm()
        return render(request, 'blog/contact.html', {'form': form})
