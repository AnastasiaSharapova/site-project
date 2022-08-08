from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def save(self, commit=True):
        user = super(NewUserForm,self).save(commit=False)

        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class RegUser(UserCreationForm):
    username = forms.CharField(label ='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label ='Пароль',widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2=forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
