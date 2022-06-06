from django.shortcuts import render,HttpResponse
from .models import Employee, Role, Department
from datetime import datetime
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request, 'index.html')

def all_emp(request):
    emp = Employee.objects.all()
    context = {
        'emps' : emp
    }
    print(context)
    return render(request, 'all_emp.html', context)

def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])
        phone = int(request.POST['phone'])
        new_emp = Employee(first_name=first_name, last_name=last_name, phone=phone, salary=salary, role_id=role, dept_id=dept, bonus=bonus, hire_date=datetime.now())
        new_emp.save()
        return HttpResponse('Employee Added!')
    elif request.method == 'GET':
        return render(request, 'add_emp.html')
    else:
        return HttpResponse('Some Error Occured !')
def remove_emp(request , emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse('Employee Removed Successfully !')
        except:
            return HttpResponse('Enter Valid Employee ID')
    emps = Employee.objects.all()
    context ={
        'emps' : emps
    }
    return render(request, 'remove_emp.html', context)

def edit_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name = name)
        if role:
            emps = emps.filter(role__name = name)

        context = {
            'emps': emps
        }
        return render(request, 'all_emp.html', context)

    elif request.method == 'GET':
        return render(request, 'edit_emp.html')
    else:
        return HttpResponse('Exception Occurred !')