from django import forms
from .models import *
from django.forms import DateInput, DateTimeInput, TimeInput, CheckboxInput, Textarea, TextInput

class GenericModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(GenericModelForm, self).__init__(*args, **kwargs)
        
        # Loop through each field in the form
        for field_name, field in self.fields.items():
            field_type = type(field)
            
            # Generic CSS class for all fields
            field.widget.attrs['class'] = 'form-control'

            # Custom widgets for specific field types
            if isinstance(field, forms.DateField):
                field.widget = DateInput(attrs={'class': 'form-control', 'type': 'date'})
            elif isinstance(field, forms.DateTimeField):
                field.widget = DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'})
            elif isinstance(field, forms.TimeField):
                field.widget = TimeInput(attrs={'class': 'form-control', 'type': 'time'})
            elif isinstance(field, forms.BooleanField):
                field.widget = CheckboxInput()
            elif isinstance(field, forms.CharField) and isinstance(field.widget, forms.Textarea):
                field.widget = Textarea(attrs={'class': 'form-control', 'rows': 3})
            elif isinstance(field, forms.CharField):
                field.widget = TextInput(attrs={'class': 'form-control'})

class UserRegistrationForm(GenericModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'password','roles','maker','checker')


class LoginForm(forms.Form):
    email=forms.EmailField()
    password=forms.CharField()

class RoleForm(GenericModelForm):
    class Meta:
        model = Role
        exclude = ('created_by','update_by','permissions')