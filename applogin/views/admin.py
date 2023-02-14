from django.shortcuts import render, redirect
from applogin import models
from applogin.utils.pagination import Pagination
from applogin.utils.BootstrapModelform import BootstrapModelform
from django import forms
from django.core.exceptions import ValidationError
from applogin.utils.encrypt import md5


def admin_list(request):
    info = request.session.get("info")
    if not info:
        return redirect('/login/')

        # 构建搜索
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["name__contains"] = search_data
    # 根据搜索条件去数据库获取
    queryset = models.Admin.objects.filter(**data_dict)

    # 分页

    page_object = Pagination(request, queryset)
    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
        "search_data": search_data
    }
    return render(request, 'admin_list.html', context)


class AdminModelForm(BootstrapModelform):
    confirm_pwd = forms.CharField(label='确认密码', widget=forms.PasswordInput)

    # widget=forms.PasswordInput(render_value=True)密码不清空

    class Meta:
        model = models.Admin
        fields = ["name", "pwd", "confirm_pwd"]
        widgets = {
            "pwd": forms.PasswordInput
        }

    def clean_pwd(self):
        pwd = self.cleaned_data.get("pwd")
        return md5(pwd)

    def clean_confirm_pwd(self):
        pwd = self.cleaned_data.get("pwd")
        comform = md5(self.cleaned_data.get("confirm_pwd"))
        if comform != pwd:
            raise ValidationError("密码不一致")
        return comform


def admin_add(request):
    title = "新建管理员"
    if request.method == 'GET':
        form = AdminModelForm()
        return render(request, 'change.html', {"form": form, "title": title})
    form = AdminModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    return render(request, 'change.html', {"form": form, "title": title})


class AdminEditModelForm(BootstrapModelform):
    class Meta:
        model = models.Admin
        fields = ['name']


def admin_edit(request, nid):
    row_object = models.Admin.objects.filter(id=nid).first()
    if not row_object:
        return redirect('/admin/list')
    title = "编辑管理员"
    if request.method == 'GET':
        form = AdminEditModelForm(instance=row_object)
        return render(request, 'change.html', {"form": form, "title": title})

    form = AdminEditModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    return render(request, 'change.html', {"form": form, "title": title})


def admin_del(request, nid):
    models.Admin.objects.filter(id=nid).delete()
    return redirect("/admin/list/")


class AdminResetModelForm(BootstrapModelform):
    confirm_pwd = forms.CharField(label='确认密码', widget=forms.PasswordInput())

    class Meta:
        model = models.Admin
        fields = ["pwd", "confirm_pwd"]
        widgets = {
            "pwd": forms.PasswordInput
        }

    def clean_pwd(self):
        pwd = self.cleaned_data.get("pwd")
        md5_pwd = md5(pwd)
        exists = models.Admin.objects.filter(id=self.instance.pk, pwd=md5_pwd).exists()
        if exists:
            raise ValidationError("不能与原密码相同")
        return md5_pwd

    def clean_confirm_pwd(self):
        pwd = self.cleaned_data.get("pwd")
        comform = md5(self.cleaned_data.get("confirm_pwd"))
        if comform != pwd:
            raise ValidationError("密码不一致")
        return comform


def admin_reset(request, nid):
    row_object = models.Admin.objects.filter(id=nid).first()
    if not row_object:
        return redirect('/admin/list')

    title = "重置密码-{}".format(row_object.name)
    if request.method == 'GET':
        form = AdminResetModelForm()
        return render(request, 'change.html', {"form": form, "title": title})

    form = AdminResetModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/admin/list')
    return render(request, 'change.html', {"form": form, "title": title})
