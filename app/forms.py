from django import forms

from .models import Note


class CreateNoteForm(forms.ModelForm):
    name = forms.CharField(max_length=80, widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Добавить заметку...'
    }))
    
    class Meta:
        model = Note
        fields = ('name', )
