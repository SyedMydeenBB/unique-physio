from django.contrib import admin
from .models import *

@admin.register(PCList)
class PCListAdmin(admin.ModelAdmin):
    list_display = ['date', 'title', 'name', 'case_number', 'diagnosis', 'treatment_1', 'treatment_2', 'treatment_3', 'charge', 'received', 'payment_status', 'payment_type', 'payment_frequency', 'therapist']

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['name', 'case_number', 'age', 'gender', 'chief_complaint', 'reference', 'contact', 'address']

@admin.register(DailySheet)
class DailySheetAdmin(admin.ModelAdmin):
    list_display = ['date', 'name', 'case_number', 'diagnosis', 'charge', 'received', 'payment_status', 'payment_type', 'payment_frequency', 'in_time', 'out_time', 'treatment_1', 'treatment_2', 'treatment_3', 'treatment_4', 'therapist_1', 'therapist_2']
