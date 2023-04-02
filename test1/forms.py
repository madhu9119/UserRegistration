from django import forms
from .models import *


class UserForm(forms.ModelForm):
    class Meta():
        model = UserRegister
        fields = "__all__"
