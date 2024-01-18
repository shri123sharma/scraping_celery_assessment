from django.contrib import admin
from .models import *

# Define the admin class
class JobDataAdmin(admin.ModelAdmin):
    list_display = ['ip_address','port','country','protocols']

admin.site.register(JobData, JobDataAdmin)