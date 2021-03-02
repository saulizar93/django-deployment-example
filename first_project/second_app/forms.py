from django import forms
from .models import User

class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


#if we had another model, it would have its own class with own Meta
