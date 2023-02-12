from django.shortcuts import render, redirect
from applogin import models
from applogin.utils.pagination import Pagination
from applogin.utils.BootstrapModelform import BootstrapModelform
from django import forms
from django.core.exceptions import ValidationError
from applogin.utils.encrypt import md5
from applogin.utils.BootstrapModelform import BootstrapForm


class LoginForm(BootstrapForm):
    username = forms.CharField(label="用户名", widget=forms.TextInput,required=True)
    password = forms.CharField(label="密码", widget=forms.PasswordInput,required=True)


# class LoginModelForm(forms.ModelForm):
#     class Meta:
#         model = models.Admin
#         fields = ["name", "pwd"]


def login(request):
    if request.method =='GET':
        form = LoginForm()
        return render(request, 'login.html', {"form": form})
    form = LoginForm(data=request.POST)
    if form.is_valid():
        pass
    return render(request, 'login.html', {"form": form})

def logout(request):
    pass

