from django.shortcuts import render
from .models import Department, Employee
from django.http import JsonResponse
from django.http import HttpResponse

def home(request):
    return render(request, "main/base.html")


def get_departments(request):
    departments = Department.objects.all().values("id", "name")
    return JsonResponse({"departments": list(departments)})


def get_employees(request, department_id):
    employees = Employee.objects.filter(department_id=department_id).exclude(position=3).values("id", "first_name", "last_name", "position")
    employee_list = [{"id": emp["id"], "name": f"{emp['first_name']} {emp['last_name']}", "position": emp["position"]} for emp in employees]
    return JsonResponse({"employees": employee_list})