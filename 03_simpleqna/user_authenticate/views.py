from django.contrib import auth, messages
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import RedirectView, FormView
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView


from simpleqna.settings import (
 EMAIL_HOST_USER
)

from .forms import LoginForm, ResetPasswordForm, SetPasswordForm, UserCreationForm
from .models import UserAuthentication


class LogInFormView(LoginView):
    form_class = LoginForm
    template_name = 'authenticate/login/user_login.html'

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        user = form.get_user()
        login(self.request, user)
        return redirect('question_details')


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'authenticate/login/signup.html'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Account created successfully. Please log in.")
        return redirect('login')



class LogOutView(RedirectView):
    def get(self, request, *args, **kwargs):
        auth.logout(request)
        messages.success(request, "You're logged out")
        return redirect('login')


def send_password_reset(subject, to, context):
    html_context = render_to_string('mail/reset_password.html', context)
    text_context = strip_tags(html_context)

    email = EmailMultiAlternatives(
        subject,
        text_context,
        EMAIL_HOST_USER,
        [to],
    )
    email.attach_alternative(html_context, "text/html")
    email.send()


# Password Update
class ForgotPassword(FormView):
    form_class = ResetPasswordForm
    template_name = 'authenticate/login/reset.html'


    def form_valid(self, form):
        email = form.cleaned_data['email']
        try:
            user = UserAuthentication.objects.get(email=email)
        except UserAuthentication.DoesNotExist:
            messages.error(self.request, 'User does not exist')
            return super().form_invalid(form)

        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))

        context = {
            'user': user,
            'token': token,
            'uid': uid,
            'protocol': self.request.scheme,
            'domain': self.request.get_host(),
        }
        send_password_reset(
            subject='QNA Password Reset',
            to=email,
            context=context,
        )
        messages.success(self.request, 'Mail Sent Successfully')
        return redirect('login')


def send_password_update_notification(subject, to, context):
    html_context = render_to_string('mail/password_updated.html', context)
    text_context = strip_tags(html_context)

    email = EmailMultiAlternatives(
        subject,
        text_context,
        EMAIL_HOST_USER,
        [to],
    )
    email.attach_alternative(html_context, "text/html")
    email.send()


class PasswordConfirmView(PasswordResetConfirmView):
    template_name = 'authenticate/login/password_reset_confirm.html'
    form_class = SetPasswordForm

    def form_valid(self, form):

        uid = self.kwargs.get('uidb64')
        try:
            uid = force_str(urlsafe_base64_decode(uid))
            user = UserAuthentication.objects.get(pk=uid)

            context = {
                'user': user,
            }
            send_password_update_notification(
                subject='HMS Password Updated',
                to=user.email,
                context=context,
            )
        except UserAuthentication.DoesNotExist:
            messages.error(self.request, 'User does not exist')
            return super().form_invalid(form)
        messages.success(self.request, 'Password Changed Successfully')
        return redirect('login')
