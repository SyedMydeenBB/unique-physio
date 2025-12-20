from django.db import models
from user_management.models import User



	
class Patient(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True)
	case_number = models.CharField(max_length=20, unique=True)
	age = models.CharField(max_length=50, blank=True, null=True)
	gender = models.CharField(
		max_length=10,
		blank=True,
		null=True,
		choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]
	)
	chief_complaint = models.TextField(blank=True, null=True)
	diagnosis = models.TextField(blank=True, null=True)
	reference = models.CharField(max_length=50, blank=True, null=True)
	contact = models.CharField(max_length=50, blank=True, null=True)
	address = models.TextField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name or "Patient"

	class Meta:
		ordering = ['-created_at']


class DailySheet(models.Model):
	patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True)
	date = models.DateField(blank=True, null=True,default="timezone.now", )
	name = models.CharField(max_length=200,blank=True, null=True ,)
	case_number = models.CharField(max_length=20,blank=True, null=True ,unique=False ,)
	diagnosis = models.TextField(blank=True, null=True,)
	charge = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True,)
	received = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True,)
	payment_status = models.CharField(max_length=20,blank=True, null=True ,choices=[('paid', 'Paid'), ('partially_paid', 'Partially_paid'), ('not_paid', 'Not_paid')],)
	payment_type = models.CharField(max_length=10,blank=True, null=True ,choices=[('qr', 'Qr'), ('cash', 'Cash')],)
	payment_frequency = models.CharField(max_length=20,blank=True, null=True ,choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly')],)
	in_time = models.TimeField(blank=True, null=True,)
	out_time = models.TimeField(blank=True, null=True,)
	explain_treatment = models.TextField(blank=True, null=True)
	feedback = models.TextField(blank=True, null=True)
	treatment_1 = models.CharField(max_length=20,blank=True, null=True ,choices=[('exercise', 'Exercise'), ('cycling', 'Cycling'), ('manual_therapy', 'Manual_therapy'), ('consultation', 'Consultation'), ('arm_ergometer', 'Arm_ergometer'), ('passive_stretching', 'Passive_stretching'), ('crepe_bandage', 'Crepe_bandage')],)
	treatment_2 = models.CharField(max_length=20,blank=True, null=True ,choices=[('exercise', 'Exercise'), ('cycling', 'Cycling'), ('manual_therapy', 'Manual_therapy'), ('consultation', 'Consultation'), ('arm_ergometer', 'Arm_ergometer'), ('passive_stretching', 'Passive_stretching'), ('crepe_bandage', 'Crepe_bandage')],)
	treatment_3 = models.CharField(max_length=20,blank=True, null=True ,choices=[('exercise', 'Exercise'), ('cycling', 'Cycling'), ('manual_therapy', 'Manual_therapy'), ('consultation', 'Consultation'), ('arm_ergometer', 'Arm_ergometer'), ('passive_stretching', 'Passive_stretching'), ('crepe_bandage', 'Crepe_bandage')],)
	treatment_4 = models.CharField(max_length=20,blank=True, null=True ,choices=[('exercise', 'Exercise'), ('cycling', 'Cycling'), ('manual_therapy', 'Manual_therapy'), ('consultation', 'Consultation'), ('arm_ergometer', 'Arm_ergometer'), ('passive_stretching', 'Passive_stretching'), ('crepe_bandage', 'Crepe_bandage')],)
	therapist_1 = models.CharField(max_length=20,blank=True, null=True ,choices=[('Basidh', 'Basidh'), ('Visitra', 'Visitra'), ('Bharatiselvi', 'Bharatiselvi')],)
	therapist_2 = models.CharField(max_length=20,blank=True, null=True ,choices=[('Basidh', 'Basidh'), ('Visitra', 'Visitra'), ('Bharatiselvi', 'Bharatiselvi')],)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return f'{self.date}'

class PCList(models.Model):
	patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True)
	date = models.DateField(blank=True, null=True,default="timezone.now", )
	name = models.CharField(max_length=200,blank=True, null=True ,)
	case_number = models.CharField(max_length=20,blank=True, null=True ,unique=False ,)
	diagnosis = models.TextField(blank=True, null=True,)
	charge = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True,)
	received = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True,)
	payment_status = models.CharField(max_length=20,blank=True, null=True ,choices=[('paid', 'Paid'), ('partially_paid', 'Partially_paid'), ('not_paid', 'Not_paid')],)
	payment_type = models.CharField(max_length=10,blank=True, null=True ,choices=[('qr', 'Qr'), ('cash', 'Cash')],)
	payment_frequency = models.CharField(max_length=20,blank=True, null=True ,choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly')],)
	in_time = models.TimeField(blank=True, null=True,)
	out_time = models.TimeField(blank=True, null=True,)
	explain_treatment = models.TextField(blank=True, null=True)
	feedback = models.TextField(blank=True, null=True)

	treatment_1 = models.CharField(max_length=20,blank=True, null=True ,choices=[('exercise', 'Exercise'), ('cycling', 'Cycling'), ('manual_therapy', 'Manual_therapy'), ('consultation', 'Consultation'), ('arm_ergometer', 'Arm_ergometer'), ('passive_stretching', 'Passive_stretching'), ('crepe_bandage', 'Crepe_bandage')],)
	treatment_2 = models.CharField(max_length=20,blank=True, null=True ,choices=[('exercise', 'Exercise'), ('cycling', 'Cycling'), ('manual_therapy', 'Manual_therapy'), ('consultation', 'Consultation'), ('arm_ergometer', 'Arm_ergometer'), ('passive_stretching', 'Passive_stretching'), ('crepe_bandage', 'Crepe_bandage')],)
	treatment_3 = models.CharField(max_length=20,blank=True, null=True ,choices=[('exercise', 'Exercise'), ('cycling', 'Cycling'), ('manual_therapy', 'Manual_therapy'), ('consultation', 'Consultation'), ('arm_ergometer', 'Arm_ergometer'), ('passive_stretching', 'Passive_stretching'), ('crepe_bandage', 'Crepe_bandage')],)
	treatment_4 = models.CharField(max_length=20,blank=True, null=True ,choices=[('exercise', 'Exercise'), ('cycling', 'Cycling'), ('manual_therapy', 'Manual_therapy'), ('consultation', 'Consultation'), ('arm_ergometer', 'Arm_ergometer'), ('passive_stretching', 'Passive_stretching'), ('crepe_bandage', 'Crepe_bandage')],)
	therapist_1 = models.CharField(max_length=20,blank=True, null=True ,choices=[('Basidh', 'Basidh'), ('Visitra', 'Visitra'), ('Bharatiselvi', 'Bharatiselvi')],)
	therapist_2 = models.CharField(max_length=20,blank=True, null=True ,choices=[('Basidh', 'Basidh'), ('Visitra', 'Visitra'), ('Bharatiselvi', 'Bharatiselvi')],)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	def __str__(self):
		return f'{self.date}'