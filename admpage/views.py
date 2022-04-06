from django.shortcuts import render,redirect
from django.http import HttpResponse
from matplotlib.style import context
from django.contrib.auth.forms import UserCreationForm

from .models import *
from .filter import *
from .forms import CreateEmpForm,workForm, siteform

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 



# Create your views here.
def rou(request):
    rou  = Worker.objects.all()
    return render(request ,"rou.html" ,{'rou':rou})




@login_required(login_url='emplog') 
def ind(request):
    att = Attendance.objects.all().order_by('-ada','-atim')[:10]
    con = Site.objects.all()[:6]
    cnt = Site.objects.all().count()

    cont = {'att':att, 'con':con, 'cnt':cnt}
    return render(request, "index.html",cont)






@login_required(login_url='emplog') 
def attendance(request):
    att = Attendance.objects.all().order_by('-ada','-atim')
    print(type(att))
    return render(request, "attendance.html",{'att':att})





@login_required(login_url='emplog') 
def workers(request):
    work = Worker.objects.all()

    mfil = workfilter(request.GET, queryset=work)
    work = mfil.qs
    
    form = workForm()
    if request.method == 'POST':
        form = workForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('name')
            messages.success(request, 'Account was created for' + user)
            return redirect('workers')


    cont = {'work':work, 'mfil':mfil,'form':form}


    return render(request, "workers.html",cont)





@login_required(login_url='emplog') 
def construction(request):
    site = Site.objects.all()
    mfil = sitefilter(request.GET, queryset=site)
    site = mfil.qs
    form = siteform()
    if request.method == 'POST':
        form = siteform(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('sname')
            messages.success(request, 'Data was created for' + user)
            return redirect('construction')

    cont = {'site':site, 'mfil':mfil, 'form':form}

    return render(request, "construction.html",cont)




@login_required(login_url='emplog') 
def paysalary(request):
    sal = Worker.objects.all()

    return render(request, "paysalary.html", {'sal':sal})





@login_required(login_url='emplog') 
def complaints(request):
    return render(request, "complaints.html")




@login_required(login_url='emplog') 
def worker_profile(request,pk):

    worker_profile = Worker.objects.get(id=pk)
    att = Attendance.objects.all().order_by('-ada','-atim')

    context = {'worker_profile':worker_profile, 'att':att}
    return render(request, "worker_profile.html", context)




@login_required(login_url='emplog') 
def construction_site_profile(request, pk):
    construction_site_profile = Site.objects.get(id=pk)
    att = Attendance.objects.all().order_by('-ada','-atim')
    context = {'construction_site_profile':construction_site_profile,'att':att}
    return render(request, "site_profile.html", context)




@login_required(login_url='emplog') 
def calculate_salary(request,pk):
    cs = Attendance.objects.get(id=pk)
    con = {'cs':cs}
    return render(request, "calculate.html",con)





def aworker(request):
    form = workForm()
    if request.method == 'POST':
        form = workForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('name')
            messages.success(request, 'Account was created for' + user)
            return redirect('workers')
        


    con = {'form':form}


    return render(request, "addworker.html",con)






def add_site(request):
    form = siteform()
    if request.method == 'POST':
        form = siteform(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('sname')
            messages.success(request, 'Data was created for' + user)
            return redirect('construction')
        


    con = {'form':form}
    return render(request, "addsite.html",con)





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


    # def reset_pass(request):

def mobindex(request):
    return render(request ,'mobindex.html')