from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.user_login, name='user_login'),

    path('pclist/', views.pclist_list, name='pclist_list'),
    path('pclist/<int:pk>/', views.pclist_detail, name='pclist_detail'),
    path('pclist/new/', views.pclist_create, name='pclist_create'),
    path('pclist/<int:pk>/edit/', views.pclist_update, name='pclist_update'),
    path('pclist/<int:pk>/delete/', views.pclist_delete, name='pclist_delete'),

    path('patient/', views.patient_list, name='patient_list'),
    path('patient/new/', views.patient_create, name='patient_create'),
    path('patient/<int:pk>/edit/', views.patient_update, name='patient_update'),
    path('patient/<int:pk>/delete/', views.patient_delete, name='patient_delete'),
    path('patient/upload/', views.upload_excel, name='upload_excel'),
    path('patient/download/', views.download_excel, name='download_excel'),

    path('dailysheet/', views.daily_sheet_list, name='daily_sheet_list'),
    path('dailysheet/new/', views.daily_sheet_create, name='daily_sheet_create'),
    path('ajax/check-case-number/', views.check_case_number),
    path('ajax/patient-followups/<int:patient_id>/', views.patient_followups),
    path('dailysheet/<int:pk>/edit/', views.daily_sheet_update, name='daily_sheet_update'),
    path('dailysheet/<int:pk>/delete/', views.daily_sheet_delete, name='daily_sheet_delete'),
    path('dailysheet/export/', views.daily_sheet_export, name='daily_sheet_export'),
    path('dailysheet/import/', views.daily_sheet_import, name='daily_sheet_import'),

]