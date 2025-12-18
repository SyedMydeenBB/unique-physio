
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from user_management.models import User
from django.shortcuts import get_object_or_404
from user_management.decorators import check_permission

def user_login(request):
    if request.method == 'POST':
        print('request.POST', request.POST)
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirect to a success page
            else:
                print('Invalid email or password')
                form.add_error(None, 'Invalid email or password')
        else:
            print('form', form.errors)
    else:
        form = LoginForm()

    context = {
        'form': form
    }
    return render(request, 'Auth/login.html', context)


def dashboard(request):
    return render(request, 'dashboard.html',{'dashboard':'active'})


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('user_login')
    else:
        return redirect('user_login')

# Create
@login_required(login_url='/')
@check_permission('pclist_create')
def pclist_create(request):
    """
    Handles the creation of a new PCList record.

    - If the request method is POST, the form data is validated and, if valid, the new record is saved.
    - If the request method is GET, an empty form is displayed.
    - Upon successful creation, redirects to the list view.
    - In case of an error, renders a custom 500 error page.
    """
    try:
        if request.method == "POST":
            form = PCListForm(request.POST)
            if form.is_valid():
                form.save()  # Save the form data as a new record
                return redirect('pclist_list')
        else:
            form = PCListForm()  # Display an empty form
        context = {
            'form': form, 'screen_name': 'PCList'
        }
        return render(request, 'create.html', context)
    except Exception as error:
        return render(request, '500.html', {'error': error})

# Read - List View
@login_required(login_url='/')
@check_permission('pclist_view')
def pclist_list(request):
    """
    Displays a list of all PCList records.

    - Fetches all records from the PCList model.
    - Passes the records to the template for rendering.
    - In case of an error, renders a custom 500 error page.
    """
    try:
        records = PCList.objects.all()
        context = {
            'records': records, 'screen_name': 'PCList'
        }
        return render(request, 'pclist_list.html', context)
    except Exception as error:
        return render(request, '500.html', {'error': error})

# Read - Detail View
@login_required(login_url='/')
@check_permission('pclist_view')
def pclist_detail(request, pk):
    """
    Displays the details of a specific PCList record.

    - Fetches the record based on the primary key (pk).
    - Passes the record to the form for viewing.
    - In case of an error, renders a custom 500 error page.
    """
    try:
        record = get_object_or_404(PCList, pk=pk)
        form = PCListForm(instance=record)
        context = {
            'screen_name': 'PCList', 'view': True, 'form': form
        }
        return render(request, 'create.html', context)
    except Exception as error:
        return render(request, '500.html', {'error': error})

# Update
@login_required(login_url='/')
@check_permission('pclist_update')
def pclist_update(request, pk):
    """
    Handles the updating of an existing PCList record.

    - If the request method is POST, the form data is validated and, if valid, the record is updated.
    - If the request method is GET, the existing record is displayed in the form.
    - Upon successful update, redirects to the list view.
    - In case of an error, renders a custom 500 error page.
    """
    try:
        pclist = get_object_or_404(PCList, pk=pk)
        if request.method == "POST":
            form = PCListForm(request.POST, instance=pclist)
            if form.is_valid():
                form.save()  # Save the updated record
                return redirect('pclist_list')
        else:
            form = PCListForm(instance=pclist)  # Display the existing record in the form
        context = {
            'form': form, 'screen_name': 'PCList'
        }
        return render(request, 'create.html', context)
    except Exception as error:
        return render(request, '500.html', {'error': error})

# Delete
@login_required(login_url='/')
@check_permission('pclist_delete')
def pclist_delete(request, pk):
    """
    Handles the deletion of an existing PCList record.

    - Fetches the record based on the primary key (pk).
    - Deletes the record from the database.
    - Upon successful deletion, redirects to the list view.
    - In case of an error, renders a custom 500 error page.
    """
    try:
        record = get_object_or_404(PCList, pk=pk)
        record.delete()  # Delete the record
        return redirect('pclist_list')
    except Exception as error:
        return render(request, '500.html', {'error': error})
# Assuming you have this decorator
def check_permission(permission_name):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            # Add your permission checking logic here
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator


@login_required(login_url='/')
@check_permission('patient_create')
def patient_create(request):
    """
    Handles the creation of a new Patient record.
    - Validates form data including duplicate case number check
    - Displays error messages if case number already exists
    """
    try:
        if request.method == "POST":
            form = PatientForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('patient_list')
            # If form is invalid (including duplicate case number), it will show errors
        else:
            form = PatientForm()
        
        context = {
            'form': form,
            'screen_name': 'Patient'
        }
        return render(request, 'create.html', context)
    except Exception as error:
        return render(request, '500.html', {'error': error})

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
@login_required(login_url='/')
@check_permission('patient_view')
def patient_list(request):
    """
    Displays a filtered list of Patient records with optional filtering
    - Supports filtering by case number, name, gender, year, and date range
    - Scrollable table (no pagination)
    """
    records = Patient.objects.all()
    
    # Initialize filter form with GET parameters
    filter_form = PatientFilterForm(request.GET or None)
    
    if filter_form.is_valid():
        case_number = filter_form.cleaned_data.get('case_number')
        if case_number:
            records = records.filter(case_number__icontains=case_number)
        
        name = filter_form.cleaned_data.get('name')
        if name:
            records = records.filter(name__icontains=name)
        
        gender = filter_form.cleaned_data.get('gender')
        if gender:
            records = records.filter(gender=gender)
        
        year = filter_form.cleaned_data.get('year')
        if year:
            records = records.filter(created_at__year=year)
        
        date_from = filter_form.cleaned_data.get('date_from')
        date_to = filter_form.cleaned_data.get('date_to')
        if date_from:
            records = records.filter(created_at__date__gte=date_from)
        if date_to:
            records = records.filter(created_at__date__lte=date_to)
    
    context = {
        'records': records,       # Full queryset
        'patients': records,      # Alias if needed
        'filter_form': filter_form,
        'screen_name': 'Patient',
        'total_count': records.count()
    }
    
    return render(request, 'patient_list.html', context)

    
@login_required(login_url='/')
@check_permission('patient_update')
def patient_update(request, pk):
    """
    Handles updating an existing Patient record.
    - Validates case number uniqueness (excluding current record)
    """
    try:
        patient = get_object_or_404(Patient, pk=pk)
        
        if request.method == "POST":
            form = PatientForm(request.POST, instance=patient)
            if form.is_valid():
                form.save()
                return redirect('patient_list')
        else:
            form = PatientForm(instance=patient)
        
        context = {
            'form': form,
            'screen_name': 'Patient'
        }
        return render(request, 'create.html', context)
    except Exception as error:
        return render(request, '500.html', {'error': error})


@login_required(login_url='/')
@check_permission('patient_delete')
def patient_delete(request, pk):
    """
    Handles deletion of a Patient record.
    """
    try:
        patient = get_object_or_404(Patient, pk=pk)
        patient.delete()
        return redirect('patient_list')
    except Exception as error:
        return render(request, '500.html', {'error': error})
import pandas as pd
from django.http import HttpResponse
from io import BytesIO


def upload_excel(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            df = pd.read_excel(file)

            # Normalize headers
            df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

            for _, row in df.iterrows():
                Patient.objects.update_or_create(
                    case_number=row.get('case_number'),
                    defaults={
                        'name': row.get('name'),
                        'age': row.get('age'),
                        'gender': row.get('gender'),
                        'chief_complaint': row.get('chief_complaint'),
                        'reference': row.get('reference'),
                        'contact': row.get('contact_number') or row.get('contact'),
                        'address': row.get('address')
                    }
                )
            return redirect('patient_list')
    else:
        form = UploadFileForm()
    return render(request, 'upload_excel.html', {'form': form})


def download_excel(request):
    patients = Patient.objects.all()
    data = {
        'Name': [p.name for p in patients],
        'Case Number': [p.case_number for p in patients],
        'Age': [p.age for p in patients],
        'Gender': [p.get_gender_display() for p in patients],
        'Chief Complaint': [p.chief_complaint for p in patients],
        'Reference': [p.reference for p in patients],
        'Contact': [p.contact for p in patients],
        'Address': [p.address for p in patients],
    }
    
    df = pd.DataFrame(data)
    output = BytesIO()
    df.to_excel(output, index=False)
    output.seek(0)
    
    response = HttpResponse(output, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=patients.xlsx'
    return response


from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import DailySheet
from .forms import DailySheetFilterForm


@login_required(login_url='/')
def daily_sheet_list(request):
    sheets = DailySheet.objects.all().order_by('-date')

    filter_form = DailySheetFilterForm(request.GET or None)

    if filter_form.is_valid():
        case_number = filter_form.cleaned_data.get('case_number')
        if case_number:
            sheets = sheets.filter(case_number__icontains=case_number)

        name = filter_form.cleaned_data.get('name')
        if name:
            sheets = sheets.filter(name__icontains=name)

        payment_status = filter_form.cleaned_data.get('payment_status')
        if payment_status:
            sheets = sheets.filter(payment_status=payment_status)

        year = filter_form.cleaned_data.get('year')
        if year:
            sheets = sheets.filter(created_at__year=year)

        date_from = filter_form.cleaned_data.get('date_from')
        if date_from:
            sheets = sheets.filter(date__gte=date_from)

        date_to = filter_form.cleaned_data.get('date_to')
        if date_to:
            sheets = sheets.filter(date__lte=date_to)

    context = {
        'sheets': sheets,
        'filter_form': filter_form,
        'total_count': sheets.count(),
        'screen_name': 'Daily Sheet'
    }
    return render(request, 'daily_sheet_list.html', context)


from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils import timezone
from django.contrib import messages
from .models import DailySheet, Patient
from .forms import DailySheetForm

from django.utils import timezone
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from .models import Patient, DailySheet
from .forms import DailySheetForm


def daily_sheet_create(request):
    if request.method == 'POST':
        form = DailySheetForm(request.POST)
        if form.is_valid():
            daily_sheet = form.save(commit=False)
            
            # Get current time
            current_time = timezone.localtime()
            
            # Auto fill in_time if case_number is provided and in_time is empty
            if daily_sheet.case_number and not daily_sheet.in_time:
                daily_sheet.in_time = current_time
                
            # Auto fill out_time if payment_status is provided and out_time is empty
            if daily_sheet.payment_status and not daily_sheet.out_time:
                daily_sheet.out_time = current_time
                
            daily_sheet.save()
            messages.success(request, 'Daily sheet entry created successfully!')
            return redirect('daily_sheet_list')
    else:
        form = DailySheetForm()
        # Set initial date to today
        form.fields['date'].initial = timezone.now().date()

    return render(request, 'daily_sheet_form.html', {'form': form})


def check_case_number(request):
    case_number = request.GET.get('case_number')

    try:
        patient = Patient.objects.get(case_number=case_number)
        return JsonResponse({
            'exists': True,
            'patient_id': patient.id,
            'name': patient.name,
            'diagnosis': patient.chief_complaint,
            'age': patient.age,
            'gender': patient.gender,
        })
    except Patient.DoesNotExist:
        return JsonResponse({'exists': False})


def patient_followups(request, patient_id):
    sheets = DailySheet.objects.filter(patient_id=patient_id).order_by('date')

    data = []
    for s in sheets:
        data.append({
            'date': s.date.strftime('%d-%m-%Y') if s.date else '',
            'treatments': ", ".join(filter(None, [
                s.treatment_1, s.treatment_2, s.treatment_3, s.treatment_4
            ])),
            'explain_treatment': s.explain_treatment,
            'feedback': s.feedback
        })

    return JsonResponse({'data': data})
def daily_sheet_update(request, pk):
    """Update an existing daily sheet entry"""
    sheet = get_object_or_404(DailySheet, pk=pk)
    
    if request.method == 'POST':
        form = DailySheetForm(request.POST, instance=sheet)
        if form.is_valid():
            form.save()
            messages.success(request, 'Daily sheet entry updated successfully!')
            return redirect('daily_sheet_list')
    else:
        form = DailySheetForm(instance=sheet)
    
    return render(request, 'daily_sheet_form.html', {'form': form, 'action': 'Update', 'sheet': sheet})

def daily_sheet_delete(request, pk):
    """Delete a daily sheet entry"""
    sheet = get_object_or_404(DailySheet, pk=pk)
    
    if request.method == 'POST':
        sheet.delete()
        messages.success(request, 'Daily sheet entry deleted successfully!')
        return redirect('daily_sheet_list')
    
    return render(request, 'daily_sheet_confirm_delete.html', {'sheet': sheet})
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment
from datetime import datetime, timedelta

from django.http import HttpResponse
from django.utils import timezone
from datetime import timedelta
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, numbers

from .models import DailySheet


def daily_sheet_export(request):
    """Export daily sheets to Excel (Safe, IST-based, Production-ready)"""

    # Base queryset
    sheets = DailySheet.objects.all()

    # Filters
    filter_type = request.GET.get('filter_type', 'all')
    custom_start = request.GET.get('custom_start')
    custom_end = request.GET.get('custom_end')

    today = timezone.localdate()

    if filter_type == 'week':
        start_date = today - timedelta(days=today.weekday())
        end_date = start_date + timedelta(days=6)
        sheets = sheets.filter(date__range=[start_date, end_date])

    elif filter_type == 'month':
        sheets = sheets.filter(date__year=today.year, date__month=today.month)

    elif filter_type == 'year':
        sheets = sheets.filter(date__year=today.year)

    elif filter_type == 'custom' and custom_start and custom_end:
        sheets = sheets.filter(date__range=[custom_start, custom_end])

    # Create workbook
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = 'Daily Sheets'

    # Headers
    headers = [
        'Date', 'Name', 'Case Number', 'Diagnosis',
        'Charge', 'Received', 'Payment Status',
        'Payment Type', 'Payment Frequency',
        'In Time', 'Out Time',
        'Treatment 1', 'Treatment 2', 'Treatment 3', 'Treatment 4',
        'Therapist 1', 'Therapist 2'
    ]

    header_fill = PatternFill(start_color='4472C4', end_color='4472C4', fill_type='solid')
    header_font = Font(bold=True, color='FFFFFF')

    for col_num, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col_num)
        cell.value = header
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal='center', vertical='center')

    # Data rows
    for row_num, sheet in enumerate(sheets, start=2):

        # Date (safe)
        date_cell = ws.cell(row=row_num, column=1)
        date_cell.value = sheet.date if sheet.date else ''
        date_cell.number_format = numbers.FORMAT_DATE_YYYYMMDD2

        ws.cell(row=row_num, column=2).value = sheet.name or ''
        ws.cell(row=row_num, column=3).value = sheet.case_number or ''
        ws.cell(row=row_num, column=4).value = sheet.diagnosis or ''

        ws.cell(row=row_num, column=5).value = float(sheet.charge) if sheet.charge else 0
        ws.cell(row=row_num, column=6).value = float(sheet.received) if sheet.received else 0

        ws.cell(row=row_num, column=7).value = sheet.get_payment_status_display() if sheet.payment_status else ''
        ws.cell(row=row_num, column=8).value = sheet.get_payment_type_display() if sheet.payment_type else ''
        ws.cell(row=row_num, column=9).value = sheet.get_payment_frequency_display() if sheet.payment_frequency else ''

        ws.cell(row=row_num, column=10).value = sheet.in_time.strftime('%H:%M') if sheet.in_time else ''
        ws.cell(row=row_num, column=11).value = sheet.out_time.strftime('%H:%M') if sheet.out_time else ''

        ws.cell(row=row_num, column=12).value = sheet.treatment_1 or ''
        ws.cell(row=row_num, column=13).value = sheet.treatment_2 or ''
        ws.cell(row=row_num, column=14).value = sheet.treatment_3 or ''
        ws.cell(row=row_num, column=15).value = sheet.treatment_4 or ''

        ws.cell(row=row_num, column=16).value = sheet.get_therapist_1_display() if sheet.therapist_1 else ''
        ws.cell(row=row_num, column=17).value = sheet.get_therapist_2_display() if sheet.therapist_2 else ''

    # Auto column width
    for col in ws.columns:
        max_length = 0
        col_letter = col[0].column_letter
        for cell in col:
            if cell.value:
                max_length = max(max_length, len(str(cell.value)))
        ws.column_dimensions[col_letter].width = min(max_length + 2, 50)

    # Response
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )

    filename = f"daily_sheets_{timezone.localtime().strftime('%Y%m%d_%H%M%S')}.xlsx"
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    wb.save(response)
    return response

def daily_sheet_import(request):
    """Import daily sheets from Excel"""
    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['excel_file']
            
            try:
                # Read Excel file
                df = pd.read_excel(excel_file)
                
                # Map payment status
                payment_status_map = {
                    'Paid': 'paid',
                    'Partially Paid': 'partially_paid',
                    'Not Paid': 'not_paid'
                }
                
                payment_type_map = {
                    'QR': 'qr',
                    'Cash': 'cash'
                }
                
                payment_frequency_map = {
                    'Daily Basis': 'daily',
                    'Weekly Basis': 'weekly',
                    'Monthly Basis': 'monthly'
                }
                
                therapist_map = {
                    'Dr. Basidh': 'dr_basidh',
                    'Dr. Visitra': 'dr_visitra',
                    'Dr. Bharatiselvi': 'dr_bharatiselvi'
                }
                
                imported_count = 0
                
                for index, row in df.iterrows():
                    try:
                        sheet = DailySheet(
                            date=pd.to_datetime(row['Date'], dayfirst=True).date(),
                            name=row['Name'],
                            case_number=str(row['Case Number']),
                            diagnosis=row['Diagnosis'],
                            charge=float(row['Charge']),
                            received=float(row['Received']),
                            payment_status=payment_status_map.get(row['Payment Status'], 'not_paid'),
                            payment_type=payment_type_map.get(row['Payment Type'], 'cash'),
                            payment_frequency=payment_frequency_map.get(row['Payment Frequency'], 'daily'),
                            in_time=pd.to_datetime(row['In Time']).time() if pd.notna(row['In Time']) else None,
                            out_time=pd.to_datetime(row['Out Time']).time() if pd.notna(row['Out Time']) else None,
                            treatment_1=row.get('Treatment 1', ''),
                            treatment_2=row.get('Treatment 2', ''),
                            treatment_3=row.get('Treatment 3', ''),
                            treatment_4=row.get('Treatment 4', ''),
                            therapist_1=therapist_map.get(row['Therapist 1'], 'dr_basidh'),
                            therapist_2=therapist_map.get(row.get('Therapist 2', ''), None) if pd.notna(row.get('Therapist 2')) else None
                        )
                        sheet.save()
                        imported_count += 1
                    except Exception as e:
                        messages.warning(request, f'Error importing row {index + 2}: {str(e)}')
                        continue
                
                messages.success(request, f'Successfully imported {imported_count} records!')
                return redirect('daily_sheet_list')
                
            except Exception as e:
                messages.error(request, f'Error reading Excel file: {str(e)}')
    else:
        form = ExcelUploadForm()
    
    return render(request, 'daily_sheet_import.html', {'form': form})
