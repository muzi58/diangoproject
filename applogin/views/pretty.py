from django.shortcuts import render, redirect
from applogin import models
from applogin.utils.pagination import Pagination
from applogin.utils.forms import PrettyModelform, PrettyEditModelform


# Create your views here.


def pretty_list(request):
    data_dict = {}
    search_data = request.GET.get('que', "")
    if search_data:
        data_dict["mobile__contains"] = search_data

    queryset = models.Prettynum.objects.filter(**data_dict)
    page_object = Pagination(request, queryset)

    context = {"search_data": search_data,

               "queryset": page_object.page_queryset,  # 分完页的数据
               "page_string": page_object.html()  # 生成的页码
               }

    return render(request, 'pretty_list.html', context)


def pretty_add(request):
    if request.method == 'GET':
        form = PrettyModelform()
        return render(request, 'pretty_add.html', {"form": form})

    form = PrettyModelform(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/pretty/list/")
    return render(request, 'pretty_add.html', {'form': form})


def pretty_edit(request, nid):
    row_object = models.Prettynum.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = PrettyEditModelform(instance=row_object)
        return render(request, 'pretty_edit.html', {"form": form})

    form = PrettyEditModelform(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/pretty/list/')
    return render(request, 'pretty_edit.html', {'form': form})


def pretty_del(request, nid):
    models.Prettynum.objects.filter(id=nid).delete()
    return redirect('/pretty/list/')


models.Prettynum.objects.filter(mobile__contains=66)
