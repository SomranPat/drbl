from django.shortcuts import render
from django.http import HttpResponse
from matplotlib.style import context

from .models import *

# Create your views here.
def rou(request):
    rou  = Worker.objects.all()
    return render(request ,"rou.html" ,{'rou':rou})



def ind(request):
    return render(request, "index.html")

def attendance(request):
    return render(request, "attendance.html")

def workers(request):
    work = Worker.objects.all()
    return render(request, "workers.html",{'work':work})

def construction(request):
    site = Site.objects.all()    
    return render(request, "construction.html",{'site':site})

def paysalary(request):
    return render(request, "paysalary.html")

def complaints(request):
    return render(request, "complaints.html")

def worker_profile(request,pk):

    worker_profile = Worker.objects.get(id=pk)

    context = {'worker_profile':worker_profile}
    return render(request, "worker_profile.html", context)


def construction_site_profile(request, pk):
    construction_site_profile = Site.objects.get(id=pk)
    context = {'construction_site_profile':construction_site_profile}
    return render(request, "site_profile.html", context)

def calculate_salary(request):
    return render(request, "calculate.html")

def add_worker(request):
    return render(request, "addworker.html")

def add_site(request):
    return render(request, "addsite.html")

def sign_in(request):
    return render(request, "signin.html")
