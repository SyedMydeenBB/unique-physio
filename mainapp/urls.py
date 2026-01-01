from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.user_login, name='user_login'),

    
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


    path('pclist/', views.pc_list_list, name='pc_list_list'),
    path('pclist/new/', views.pc_list_create, name='pc_list_create'),
    path('ajax/check-pc-number/', views.check_pc_number),
    path('ajax/patient-pc-followups/<int:patient_id>/', views.patient_pc_followups),
    path('pclist/<int:pk>/edit/', views.pc_list_update, name='pc_list_update'),
    path('pclist/<int:pk>/delete/', views.pc_list_delete, name='pc_list_delete'),
    path('pclist/export/', views.pc_list_export, name='pc_list_export'),
    path('pclist/import/', views.pc_list_import, name='pc_list_import'),


    path("payment_dashboard/", views.payment_dashboard, name="payment_dashboard"),
    path("pending/", views.pending_list, name="pending_list"),
    path("advance/", views.advance_list, name="advance_list"),
    path("ledger/<int:patient_id>/", views.patient_ledger_view, name="patient_ledger"),
    path("monthly/", views.monthly_summary, name="monthly_summary"),
    path("yearly/", views.yearly_summary, name="yearly_summary"),

# pc_payment_urls.py OR same urls.py

    path("pc/payment-dashboard/", views.pc_payment_dashboard, name="pc_payment_dashboard"),
    path("pc/pending/", views.pc_pending_list, name="pc_pending_list"),
    path("pc/advance/", views.pc_advance_list, name="pc_advance_list"),
    path("pc/ledger/<int:patient_id>/", views.pc_patient_ledger, name="pc_patient_ledger"),
    path("pc/monthly/", views.pc_monthly_summary, name="pc_monthly_summary"),
    path("pc/yearly/", views.pc_yearly_summary, name="pc_yearly_summary"),

    

]