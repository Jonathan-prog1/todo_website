from django import forms
from .models import Todo


class TaskForm(forms.ModelForm):
    title = forms.CharField(
        label='', widget=forms.TextInput(attrs={'placeholder': 'Add Task here...'}))

    class Meta:
        model = Todo
        fields = ['title', 'description']


class UpdateTaskForm(forms.ModelForm):
    title = forms.CharField(
        label='Edit Task', widget=forms.TextInput(attrs={}))

    class Meta:
        model = Todo
        fields = '__all__'