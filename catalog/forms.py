from django import forms
from .models import Employee


class PublisherForm(forms.Form):
    name = forms.CharField(label="Name", max_length=50)
    email = forms.EmailField(label="Email", max_length=50)
    contact = forms.CharField(label="Contacts", max_length=50, required=False)


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
