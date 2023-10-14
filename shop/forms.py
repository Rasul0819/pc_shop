from django import forms
from .models import CustomUser


class SignUpForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())

