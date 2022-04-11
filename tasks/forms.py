from django.forms import ModelForm
from .models import Task
from django import forms


class Todo(ModelForm):

    class Meta:
        model = Task
        fields = '__all__'

        labels = {
            "title": ""
        }
