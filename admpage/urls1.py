from re import template
from django import views
from django.urls import path
from .import views

from django.contrib.auth import views as av


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
    path("calculate_salary/<str:pk>", views.calculate_salary, name = "calculate_salary"),
    path("rou", views.rou, name ="rou"),
    path("aworker", views.aworker, name ="aworker"),
    path("add_site", views.add_site, name ="add_site"),
    path("emplog", views.emplog, name ="emplog"),
    path("logout", views.logoutuser, name ="logout"),    
    path('empreg',views.empreg, name = "empreg"),
    path('mainind',views.mainind, name ='mainind' ),
    path('g2',views.g2, name = 'g2'),
    path('consg1/<str:pk>', views.consg1, name = 'consg1'),
    path('workg1/<str:pk>', views.workg1, name = 'workg1'),
    path('payment',views.payment, name = 'payment'),
    path('view_complaint/<str:pk>',views.view_complaint, name='view_complaint'),
    

    path('worlog',views.worlog, name="worlog"),
    path('mobindex',views.mobindex, name="mobindex"),
    path('mobcalculate',views.mobcalculate, name="mobcalculate"),
    path('mobcomplaint',views.mobcomplaint, name="mobcomplaint"),
    path('mobsendcomplaint',views.mobsendcomplaint, name="mobsendcomplaint"),
    path('mobviewcomplaint/<str:pk>',views.mobviewcomplaint, name="mobviewcomplaint"),
    path('mobattendance',views.mobattendance, name="mobattendance"),

    
    path('reset_pass', av.PasswordResetView.as_view(
        template_name='reset_pass.html'), name = "reset_password"),
    
    path('reset_pass_sent', av.PasswordResetDoneView.as_view(
        template_name ='reset_pass_sent.html'
    ), name = 'password_reset_done'),
    path('reset/<uidb64>/<token>/', av.PasswordResetConfirmView.as_view(
        template_name ='reset.html'
    ),name ='password_reset_confirm'),
    
    path('reset_pass_comp', av.PasswordResetCompleteView.as_view(
        template_name ='reset_done.html'
    ), name = 'password_reset_complete' ),



]