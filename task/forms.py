from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'textfield', }))

    class Meta:
        model = Task
        fields = ['title']
