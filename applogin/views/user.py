from django.shortcuts import render, redirect
from applogin import models
from applogin.utils.pagination import Pagination
from applogin.utils.forms import UserModelForm


# Create your views here.


def user_list(request):
    info = request.session.get("info")
    if not info:
        return redirect('/login/')

    # insert into applogin_userinfo(name, password, age, accent, create_time, gender, depart_id) values()
    queryset = models.Userinfo.objects.all()
    page_object = Pagination(request, queryset)
    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.html()
    }
    return render(request, 'user_list.html', context)


def user_add(request):
    info = request.session.get("info")
    if not info:
        return redirect('/login/')

    if request.method == 'GET':
        context = {
            "gender_choice": models.Userinfo.gender_choice,
            "depart_list": models.Department.objects.all(),
        }
        return render(request, 'user_add.html', context)

    user = request.POST.get('user')
    pwd = request.POST.get('pwd')
    age = request.POST.get('age')
    acc = request.POST.get('acc')
    ctime = request.POST.get('ctime')
    sex = request.POST.get('sex')
    dep = request.POST.get('dep')
    models.Userinfo.objects.create(name=user, password=pwd, age=age, accent=acc, create_time=ctime, gender=sex,
                                   depart_id=dep)
    return redirect("/user/list/")


def user_modelform_add(request):
    info = request.session.get("info")
    if not info:
        return redirect('/login/')

    if request.method == 'GET':
        form = UserModelForm()
        return render(request, 'user_modelform.html', {"form": form})

    form = UserModelForm(data=request.POST)

    if form.is_valid():
        form.save()
        return redirect("/user/list/")
    return render(request, 'user_modelform.html', {'form': form})


def user_edit(request, nid):
    info = request.session.get("info")
    if not info:
        return redirect('/login/')

    row_object = models.Userinfo.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = UserModelForm(instance=row_object)
        return render(request, 'user_edit.html', {"form": form})

    form = UserModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/user/list/')
    return render(request, 'user_edit.html', {'form': form})


def user_del(request, nid):
    info = request.session.get("info")
    if not info:
        return redirect('/login/')

    models.Userinfo.objects.filter(id=nid).delete()
    return redirect('/user/list/')
