from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views


# user register view logic
class RegisterUser(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'account created for { username } now you can login')
            return redirect('users:login')
        return render(request, 'users/register.html', {'form': form})


@login_required()
def profile(request):
    return render(request, 'users/profile.html')


@login_required()
def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'your profile has been updated')
            return redirect('users:profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {'u_form': u_form, 'p_form': p_form}
    return render(request, 'users/profile_update.html', context)


# public profile seed by any one
def public_profile(request):
    return render(request, 'users/public_profile.html')


# sections for password reset
class PasswordReset(views.PasswordResetView):
    template_name = 'users/password_rest.html'
    success_url = reverse_lazy('users:password_rest_done')


class PasswordRDone(views.PasswordResetDoneView):
    template_name = 'users/password_rest_done.html'


class PasswordRConfirm(views.PasswordResetConfirmView):
    template_name = 'users/password_rest_confirm.html'
    success_url = reverse_lazy('users:password_rest_complete')


class PasswordRComplete(views.PasswordResetCompleteView):
    template_name = 'users/password_rest_complete.html'

