import os
import uuid

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.db import transaction
from manage.models import Employee


# Create your views here.


def main(request):
    employee = Employee.objects.all()
    if employee:
        num = request.GET.get('num', 1)
        pagtor = Paginator(Employee.objects.all(), per_page=3)
        if int(num) not in pagtor.page_range:
            num = 1
        page = pagtor.page(num)
        return render(request, 'emplist.html', {'page': page})
    else:
        return render(request, 'emplist.html')


def add_employee(request):
    num = request.GET.get('num')
    return render(request, 'addEmp.html')


def confirm_add(request):
    name = request.POST.get('name')
    salary = request.POST.get('salary')
    age = request.POST.get('age')
    pic = request.FILES.get('pic')
    ext_name = os.path.splitext(pic.name)[1]
    pic.name = str(uuid.uuid4()) + ext_name
    with transaction.atomic():
        Employee.objects.create(name=name, salary=salary, age=age, pic=pic)
        pagnot = Paginator(Employee.objects.all(),per_page=3)
        num = str(pagnot.num_pages)
        url = reverse('manage:main')+"?num"+num
        return redirect(url)


def delete(request):
    pk = request.GET.get('id')
    num = request.GET.get('num')
    employee = Employee.objects.get(pk=pk)
    employee.delete()
    url = reverse('manage:main')+"?num="+num    # 反向解析
    return redirect(url)


def update(request):
    id = request.GET.get('id')
    num = request.GET.get('num')
    request.session['num'] = num
    employee = Employee.objects.filter(pk=id)
    return render(request, 'updateEmp.html', {'employee': employee})


def confirm_update(request):
    num = request.session.get('num')
    pk = request.GET.get('id')
    name = request.POST.get('name')
    salary = request.POST.get('salary')
    age = request.POST.get('age')
    pic = request.FILES.get('pic')
    employee = Employee.objects.get(pk=pk)
    employee.name = name
    employee.salary = salary
    employee.age = age
    if pic:
        pic.name = str(uuid.uuid4()) + os.path.splitext(pic.name)[1]
        employee.pic = pic
    employee.save()

    return redirect('/manage/main/?num=' + num)
