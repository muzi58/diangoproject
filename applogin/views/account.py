from django.shortcuts import render, redirect, HttpResponse
from applogin import models
from django import forms
from applogin.utils.encrypt import md5
from applogin.utils.BootstrapModelform import BootstrapForm
from applogin.utils.code import check_code
from io import BytesIO


class LoginForm(BootstrapForm):
    name = forms.CharField(label="用户名", widget=forms.TextInput, required=True)
    pwd = forms.CharField(label="密码", widget=forms.PasswordInput, required=True)
    code = forms.CharField(label="验证码", widget=forms.TextInput, required=True)

    def clean_pwd(self):
        pwd = self.cleaned_data.get("pwd")
        return md5(pwd)


def login(request):
    """登录"""
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {"form": form})
    form = LoginForm(data=request.POST)
    # 验证成功获取到用户名和密码
    if form.is_valid():
        varify_code = form.cleaned_data.pop('code')
        image_code = request.session.get("image_code", "")

        if image_code.upper() != varify_code.upper():
            form.add_error("code", "验证码错误")
            return render(request, 'login.html', {"form": form})

        # 去数据库校验用户名和密码是否在正确
        admin_object = models.Admin.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            form.add_error("pwd", "用户名或密码错误")
            return render(request, 'login.html', {"form": form})
        request.session["info"] = {"id": admin_object.id, "name": admin_object.name}

        # 设置session 7 天失效
        request.session.set_expiry(60 * 60 * 24 * 7)

        return redirect('/admin/list/')
    return render(request, 'login.html', {"form": form})


def image_code(request):
    """验证码"""
    img, code_string = check_code()
    # 调用pillow函数生成图片

    # 写进session中以便以后再次输入验证码
    request.session['img_code'] = code_string
    # 设置超时60s
    request.session.set_expiry(60)

    stream = BytesIO()
    img.save(stream, 'png')
    return HttpResponse(stream.getvalue())


def logout(request):
    """注销"""
    request.session.clear()
    return redirect('/login/')
