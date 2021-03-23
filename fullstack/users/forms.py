from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    # the extra we add fields
    email = forms.EmailField()
    email.widget.attrs['placeholder'] = "Your email address"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update(
            {'placeholder': 'Create a password'})
        self.fields['password2'].widget.attrs.update(
            {'placeholder': 'Repeat the password'})
        self.fields['username'].widget.attrs.update(
            {'placeholder': 'Username'})

    class Meta:

        model = User
        fields = ['username', 'email']
