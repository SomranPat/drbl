from django.shortcuts import render,redirect
from django.http import HttpResponse
from matplotlib.style import context
from django.contrib.auth.forms import UserCreationForm

from rbl1.settings import RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY

from .models import *
from .filter import *
from .forms import CreateEmpForm,workForm, siteform

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 


from django.shortcuts import render
from django.db.models import Count
from django.http import JsonResponse
import datetime


import razorpay



# Create your views here.
def rou(request):
    sitecnt=[]    
    cnt =[] 
    si = Site.objects.all().values_list('id','sname')
    reg = Attendance.objects.values('site_id').annotate(
        c=Count('site_id')).order_by('site_id')[:4]
    
    
    
    for j in range(len(reg)):
        cnt.append(reg[j]['c'])    



    for i in range(len(si)):
        sitecnt.append({si[i][1]:cnt[i]})
    print(sitecnt)



    rou  = Worker.objects.all()
    return render(request ,"rou.html" ,{'rou':rou})


def mainind(request):
    dtcnt=[]    
    # dt =[] 
    # si = Site.objects.all().values_list('id','sname')
    reg = Attendance.objects.values('ada').annotate(
        c=Count('ada')).order_by('-ada')[:5]    
    
    # print(reg)
    
    for j in range(len(reg)):
        t = reg[j]['ada']
        # t.strftime('%d/%m/%Y')
        # dt.appen(reg[j]['c'])
        dtcnt.append({t.strftime('%d/%m/%Y'):reg[j]['c']})
    
    # print(dtcnt)


    # for i in range(len(si)):
    #     sitecnt.append({si[i][1]:cnt[i]})
    # print(sitecnt)
    return JsonResponse(dtcnt, safe=False)


@login_required(login_url='emplog') 
def ind(request):
    att = Attendance.objects.all().order_by('-ada','-atim')[:10]
    con = Site.objects.all()[:6]
    cnt = Site.objects.all().count()

    pls =[]
    rec =[]
    
    # pltyatt = Attendance.objects.all().order_by('-ada')[:50]
    # pltxsite = Site.objects.all().values_list('id','sname')

    
    cont = {'att':att, 'con':con, 'cnt':cnt, }
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
    cs = Worker.objects.get(id=pk)
    att = Attendance.objects.all().order_by('-ada')
    

    

    if request.method =='POST':
        month = request.POST.get('mth')
        year = request.POST.get('yr')
        cnt=0
        # print(type(month))
        for a in att:
            if a.worker_id == cs.id :
                dt = a.ada
                # print(dt.strftime('%m'))

                if dt.strftime('%Y')==year and dt.strftime('%m')==month:
                    cnt+=1
        # print(cnt)
        amt = cnt*cs.spd
        cont={'cnt':cnt ,'amt':amt,'cs':cs, 'att':att}
        return render(request,"calculate.html",cont )
    # print(cnt)
    # amt = cnt*cs.spd

    #  'cnt':cnt ,'amt':amt




    con = {'cs':cs, 'att':att }
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

def mobcomplaint(request):
    return render(request ,"mobcomplaint.html")


def payment(request):
    client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))

    o_amount= 10000
    o_currency= "INR"
     
    pay_ord =client.order.create(dict(amount=o_amount,currency=o_currency,payment_capture = 1))

    pay_ord_id = pay_ord['id']

    cont = {
        'amount':100,
        'api_key':RAZORPAY_API_KEY,
        'order_id':pay_ord_id,
    }


    return render(request,'payment.html',cont)