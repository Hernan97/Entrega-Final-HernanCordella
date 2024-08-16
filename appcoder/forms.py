from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Comment, Profile, Post

class LoginForm(AuthenticationForm):
    pass

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'rating']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add your comment here...'}),
            'rating': forms.RadioSelect(choices=[(i, f"{i} Star{'s' if i > 1 else ''}") for i in range(1, 6)]),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'introduction', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'introduction': forms.Textarea(attrs={'placeholder': 'Introduction'}),
            'content': forms.Textarea(attrs={'placeholder': 'Content'}),
        }
    image = forms.ImageField(required=False)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'first_name', 'last_name', 'email', 'birth_date', 'profession']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }