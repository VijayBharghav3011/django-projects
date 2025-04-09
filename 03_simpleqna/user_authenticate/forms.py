from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm
from django.core.exceptions import ValidationError
from .validation import validate_password
from .models import UserAuthentication


class LoginForm(forms.Form):
    username_or_email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter Username or Email',
                'id': 'username_or_email'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Enter Password',
                'id': 'password'
            }
        )
    )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        username_or_email = self.cleaned_data.get('username_or_email')
        password = self.cleaned_data.get('password')

        if username_or_email and password:
            user = authenticate(username=username_or_email, password=password)

            if not user:
                user = authenticate(email=username_or_email, password=password)

            if not user:
                raise ValidationError('Invalid username, email or password')

            if not getattr(user, 'is_verified', True):
                raise ValidationError('Account Not verified')

            self.user_cache = user
        return self.cleaned_data

    def get_user(self):
        return getattr(self, 'user_cache', None)


class ResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Enter Email ID',
                'id': 'email',
                'name': 'email'
            }
        )
    )


class SetPassword(SetPasswordForm):

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match.')

        try:
            validate_password(password2)
        except ValidationError as e:
            raise forms.ValidationError(e.messages)

        return password2



class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'})
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'})
    )

    class Meta:
        model = UserAuthentication
        fields = ['username', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Enter username'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter first name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter last name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter email address'

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user