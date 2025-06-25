from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['planet_name', 'character_name', 'ship_name', 'verb']
        widgets = {
            'planet_name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Planet'}),
            'character_name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Character'}),
            'ship_name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Ship'}),
            'verb': forms.Select(choices=[('hunt', 'hunt'), ('kill', 'kill'), ('capture', 'capture')]),
        }