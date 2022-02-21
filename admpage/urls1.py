from django import views
from django.urls import path
from .import views

urlpatterns = [
    path("", views.ind, name = "ind"),
    path("home",views.ind, name = "ind"),
    path("attendance", views.attendance, name = "attendance"),
    path("workers", views.workers, name = "workers"),
    path("construction", views.construction, name = "construction"),
    path("paysalary", views.paysalary, name = "paysalary"),
    path("complaints", views.complaints , name = "complaints"),
    path("worker_profile/<str:pk>", views.worker_profile, name = "worker_profile"),
    path("construction_site_profile/<str:pk>", views.construction_site_profile, name = "construction_site_profile"),
    path("calculate_salary", views.calculate_salary, name = "calculate_salary"),
    path("rou", views.rou, name ="rou"),
    path("add_worker", views.add_worker, name ="add_worker"),
    path("add_site", views.add_site, name ="add_site"),
    path("emplog", views.emplog, name ="emplog"),
    path("logout", views.logoutuser, name ="logout"),    
    path('empreg',views.empreg, name = "empreg")
]