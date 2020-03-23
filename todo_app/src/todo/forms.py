from django import forms
from django.forms import ModelForm

from .models import *


class TaskForm(forms.ModelForm):
    description = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Add Todo item'}))

    class Meta:
        model = Task
        fields = '__all__'
