from django.shortcuts import render,redirect
from applogin import models
from applogin.utils.pagination import Pagination



# Create your views here.

def depart_list(request):
    queryset = models.Department.objects.all()
    page_object = Pagination(request, queryset)
    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.html()
    }
    return render(request, 'depart_list.html', context)


def depart_list_add(request):
    if request.method == 'GET':
        return render(request, 'depart_list_add.html')
    title = request.POST.get("title")

    models.Department.objects.create(tittle=title)

    return redirect('/depart/list/')


def depart_list_del(request):
    nid = request.GET.get('nid')
    models.Department.objects.filter(id=nid).delete()
    return redirect('/depart/list/')


def depart_edit(request, nid):
    if request.method == 'GET':
        row_object = models.Department.objects.filter(id=nid).first()
        return render(request, 'depart_edit.html', {"row_object": row_object})

    title = request.POST.get("title")
    models.Department.objects.filter(id=nid).update(tittle=title)
    return redirect('/depart/list/')
