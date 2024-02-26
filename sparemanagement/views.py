from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee, Supplier

# Create your views here.

def home(request):
    return render(request, 'sparemanagement/index.html')


def employee(request):  
    data = Employee.objects.all()
    content = {'data': data}

    return render(request, 'sparemanagement/empoyee.html', content)

def supplier(request):
    data = Supplier.objects.all()
    content = {'data': data}
    return render(request, 'sparemanagement/supplier.html', content )