from django.db import models
from .models import Task
from django.forms import ModelForm, widgets, TextInput


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets ={
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'введите название'
            }),
            "task": widgets.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'введите описание'
            }),
        }