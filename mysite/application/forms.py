from django import forms
from .models import application_user, notes



class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = application_user
        fields = ['birth_date', 'status', 'biography']

class UserDeleteForm(forms.ModelForm):
    class Meta:
        model = application_user
        fields = ['birth_date', 'status', 'biography']

class NoteCreateForm(forms.ModelForm):
    class Meta:
        model = notes
        fields = ['date', 'title', 'text','author']

class NoteUpdateForm(forms.ModelForm):
    class Meta:
        model = notes
        fields = ['date', 'title', 'text','author']

class NoteDeleteForm(forms.ModelForm):
    class Meta:
        model = notes
        fields = ['date', 'title', 'text','author']

class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = application_user
        fields = ['username', 'password', 'birth_date', 'biography']