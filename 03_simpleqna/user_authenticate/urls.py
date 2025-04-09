from django.contrib.auth.views import PasswordResetDoneView
from django.urls import path
from .views import  LogInFormView, LogOutView, ForgotPassword, PasswordConfirmView, SignUpView

urlpatterns = [

    path('', LogInFormView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),

    path('password-reset/', ForgotPassword.as_view(), name='reset_password'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/<uidb64>/<token>', PasswordConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_complete'),

]

