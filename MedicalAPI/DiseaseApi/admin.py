from django.contrib import admin
from DiseaseApi.models import PatientDetails
# Register your models here.

class PatientDetailsAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone','email','symptoms','created']


admin.site.register(PatientDetails,PatientDetailsAdmin)