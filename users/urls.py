from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [

    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile_update/', views.profile_update, name='profile_update'),
    path('public_profile/', views.public_profile, name='public_profile'),
    path('password_reset/', views.PasswordReset.as_view(), name='password_rest'),
    path('password_reset/done/', views.PasswordRDone.as_view(), name='password_rest_done'),
    path('reset/<uidb64>/<token>/', views.PasswordRConfirm.as_view(), name='password_rest_confirm'),
    path('reset/done/', views.PasswordRComplete.as_view(), name='password_rest_complete'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='users/password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done')

]

