from django import forms
from .models import Company

class CompanyForm(forms.ModelForm):
	class Meta:
		model = Company
		fields='__all__'
		widgets={
			'name': forms.TextInput(attrs={'class':'form-control'}),
			'phone_number': forms.TextInput(attrs={'class':'form-control'}),
			'address': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.EmailInput(attrs={'class':'form-control'}),
			'logo': forms.FileInput(attrs={'class':'form-control'}),
			
		}


