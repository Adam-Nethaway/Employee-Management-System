from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("get-departments/", views.get_departments, name="get_departments"),
    path("get-employees/<int:department_id>/", views.get_employees, name="get_employees"),
]
