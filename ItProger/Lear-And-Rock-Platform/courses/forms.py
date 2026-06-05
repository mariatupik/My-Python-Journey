from django import forms
from django.contrib.auth.models import User
from .models import Course, Comment, Lesson
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email*", required=True)

    class Meta:
        model = User
        fields = ['username', 'email']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class CourseAddForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['slug', 'title', 'description', 'image']
        labels = {
            'slug': 'URL Name',
            'title': 'Назва курсу',
            'description': 'Опис курсу',
            'image': 'Зображення курсу',
        }

class LessonAddForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'slug', 'video_url', 'text', 'order']
        labels = {
            'title': 'Назва уроку',
            'slug': 'URL-адреса',
            'video_url': 'Посилання на відео',
            'text': 'Текст уроку',
            'order': 'Порядок відображення',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Назва уроку'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'video_url': forms.URLInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = True 

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['user', 'lesson', 'text']
        widgets = {
            'user': forms.HiddenInput(),
            'lesson': forms.HiddenInput(),
            'text': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Напишіть свій коментар...',
                'class': 'comment-textarea',
            }),
        }
