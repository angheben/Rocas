from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Post, Draft, Comment


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': ' Your username',
        'class': 'w-full py-4 px-6 rounded-xl mb-6'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': ' Your Password',
        'class': 'w-full py-4 px-6 rounded-xl mb-6'
    }))


class SignupForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': ' Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'person@mail.com',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': ' Your Password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': ' Repeat Password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Title',
                'class': 'w-full py-4 px-6 rounded-xl'
            }),
            'image': forms.FileInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl'
            }),
            'content': forms.Textarea(attrs={
                'placeholder': 'Content',
                'class': 'w-full py-4 px-6 rounded-xl'
            }),
        }


class DraftForm(forms.ModelForm):
    class Meta:
        model = Draft
        fields = ['title', 'image', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Title',
                'class': 'w-full py-4 px-6 rounded-xl'
            }),
            'image': forms.FileInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl'
            }),
            'content': forms.Textarea(attrs={
                'placeholder': 'Content',
                'class': 'w-full py-4 px-6 rounded-xl'
            }),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
