from pyexpat import model
from unicodedata import category
from django.db import models
from sympy import true



# Create your models here.
class Site(models.Model):
    STATUS =(
        ('Active','Active'),
        ('Unactive','Unactive'),
        ('Finished','Finished',),
    )

    sname = models.CharField(max_length=200,null=True)
    status = models.CharField(max_length=10,null=True,choices=STATUS)
    location = models.CharField(max_length=300,null=True)
    city = models.CharField(max_length=100,null=True)
    contact = models.CharField(max_length=20,null=True)
    # att = models.ManyToManyField(Attendance)

    def __str__(self):
        return self.sname



class Worker(models.Model):
    CATE = (
        ('Carpenter','Carpenter'),
        ('Helper','Helper'),
        ('Electrician','Electrician'),
        ('Plasterer','Plasterer'),
        ('Welder','Welder'),
        ('Plumber','Plumber'),
        ('Glazier','Glazier'),
        ('Mason','Mason'),
        ('Concrete Finisher','Concrete Finisher'),
        ('Painter','Painter'),
        ('Other','Other'),
    )
    
    lsd = models.DateTimeField(auto_now_add=True,null=True)
    category = models.CharField(max_length=20,null=True,choices=CATE)
    name = models.CharField(max_length=20,null=True)    
    spd = models.FloatField(null=True)
    age = models.CharField(max_length=20,null=True)
    wadd = models.CharField(max_length=200,null=True)
    sdate = models.DateTimeField(auto_now_add=True,null=True)   
    # wpropic = models.ImageField(null=True, blank=True)
    wcontact = models.CharField(max_length=20,null=True)
    
    


    def __str__(self):
        return self.name

class Employe(models.Model):
    ename = models.CharField(max_length=30,null=True)
    contact = models.CharField(max_length=20,null=True)
    address = models.CharField(max_length=200,null=True)

class Attendance(models.Model):
    ada = models.DateField(auto_now_add=False,null=True)
    atim = models.TimeField(auto_now_add=False, null =True)
    worker = models.ForeignKey(Worker, null = True, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, null = True, on_delete=models.CASCADE)


# class Salary(models.Model):
#     contact = models.CharField(max_length=20,null=True)
#     amount = models.CharField(max_length=20,null=True)
#     sdate = models.DateTimeField(auto_now_add=True,null=True)    
#     employee = models.ForeignKey(Employe, null = True, on_delete=models.SET_NULL)
    
#     worker = models.ForeignKey(Worker, null = True, on_delete=models.SET_NULL)
    
#     def __str__(self):
#         return str(self.worker)

class Grievance(models.Model):
    STATUS =(
        ('Active','Active'),
        ('Unactive','Unactive'),
        ('Finished','Finished',),
    )

    worker = models.ForeignKey(Worker, null = True, on_delete=models.SET_NULL)
    g_title =  models.CharField(max_length=100,null=True)
    g_details =  models.CharField(max_length=500,null=True)
    g_status =  models.CharField(max_length=20,null=True,choices=STATUS)
    g_date = models.DateTimeField(auto_now_add=True,null=True)
    sender = models.ForeignKey(Employe, null = True, on_delete=models.SET_NULL)

class complan_chat(models.Model):
    grieve = models.ForeignKey(Grievance, null = True, on_delete=models.SET_NULL)
    msg = models.CharField(max_length=500,null=True)
    sender = models.ForeignKey(Employe, null = True, on_delete=models.SET_NULL)
    dtim = models.DateTimeField(auto_now_add=True,null=True)