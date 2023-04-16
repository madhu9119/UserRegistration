from django import forms
from .models import *
from django.forms import CharField


class UserForm(forms.ModelForm):
    # print("hddddddddddddddddd")
    name = forms.CharField(widget=forms.TextInput(attrs={'pattern':'[a-zA-Z]+'}),required=True,max_length=250)
    loginid = forms.CharField(widget=forms.TextInput(attrs={'pattern':'[a-zA-Z]+'}),required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'pattern':'(?*.=\d)(!?#$*.=[a-z])(!@#$*.=[A-Z].{8,})','title':'Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters'}),required=True)
    mobile = forms.CharField(widget=forms.TextInput(attrs={'pattern':'[564789][0-9]{9}'}),required=True)
    email = forms.CharField(widget=forms.TextInput(attrs={'pattern':'[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$'}),required=True)
    locality = forms.CharField(widget=forms.TextInput(),required=True)
    city = forms.CharField(widget=forms.TextInput(),required=True)
    state = forms.CharField(widget=forms.TextInput(),required=True)

    class Meta():
        model = UserRegister
        # print(model)
        fields = "__all__"

