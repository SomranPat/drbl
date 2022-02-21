from django.shortcuts import render,redirect
from django.http import HttpResponse
from matplotlib.style import context
from django.contrib.auth.forms import UserCreationForm

from .models import *
from .filter import *
from .forms import CreateEmpForm

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 

# Create your views here.
def rou(request):
    rou  = Worker.objects.all()
    return render(request ,"rou.html" ,{'rou':rou})


@login_required(login_url='emplog') 
def ind(request):
    return render(request, "index.html")



@login_required(login_url='emplog') 
def attendance(request):
    return render(request, "attendance.html")

@login_required(login_url='emplog') 
def workers(request):
    work = Worker.objects.all()
    mfil = workfilter(request.GET, queryset=work)
    work = mfil.qs


    cont = {'work':work, 'mfil':mfil}


    return render(request, "workers.html",cont)

@login_required(login_url='emplog') 
def construction(request):
    site = Site.objects.all()
    mfil = sitefilter(request.GET, queryset=site)
    site = mfil.qs
    cont = {'site':site, 'mfil':mfil}

    return render(request, "construction.html",cont)

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

def emplog(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password= password)
        if user is not None:
            login(request, user)
            return redirect('ind')
        
        else:
            messages.info(request, 'Username or Password is incorrect')
    
    conte = {}

    return render(request, "emplog.html",conte)

def logoutuser(request):
    logout(request)
    return redirect('emplog')

def empreg(request):
    form = CreateEmpForm()

    if request.method == 'POST':
        form = CreateEmpForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for' + user)
            
            return redirect('ind')
    
    context ={'form':form}
    return render(request, "empreg.html",context)