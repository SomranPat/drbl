from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(Site)
admin.site.register(Worker)
admin.site.register(Employe)
admin.site.register(Attendance)
# admin.site.register(Salary)


# 'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'WMS3',
#         'USER':'postgres',
#         'PASSWORD':'fudge1212',
#         'HOST':'localhost',
#         'PORT':'5432'