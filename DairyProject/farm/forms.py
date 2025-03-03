from datetime import timezone
from django.core.validators import RegexValidator
from django import forms
from django.forms.widgets import DateTimeInput
from .models import Appointment, Cattle, CustomerEditProfile, DeliveryBoyEditProfile,Insurance,Vaccination,SellerEditProfile,Breed,CattleType,ContactMessage,VetEditProfile
from django.core.exceptions import ValidationError

class CustomerRegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    phone = forms.CharField(max_length=15)

class SellerRegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    mobile = forms.CharField(max_length=15)
    farmer_license = forms.CharField(max_length=7, validators=[
        RegexValidator(
            regex=r'^F\d{5}$',
            message='Seller license must be in the format FXXXXX, where X is a digit (0-9).',
        ),
    ])

class SellerProfileForm(forms.ModelForm):
    class Meta:
        model = SellerEditProfile
        fields = '__all__'
class SellerEditProfileForm(forms.ModelForm):
    class Meta:
        model = SellerEditProfile
        fields = '__all__'
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'gender': forms.Select(choices=[('---', '---'), ('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')]),
        }
class CustomerEditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomerEditProfile
        fields = '__all__'
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'gender': forms.Select(choices=[('---', '---'), ('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')]),
        }
class BreedForm(forms.ModelForm):
    class Meta:
        model = Breed
        fields = ['cattle_type', 'name', 'status']
        widgets = {
            'cattle_type': forms.Select(choices=[
                ('Cow', 'Cow'),
                ('Goat', 'Goat'),
                ('Buffalo', 'Buffalo'),
            ]),
        }

class CattleForm(forms.ModelForm):
    class Meta:
        model = Cattle
        exclude = ['user', 'seller', 'vaccination', 'insurance']
        widgets = {
            'CattleType': forms.Select(),
            'BreedName': forms.Select(),
            'feed': forms.Select(choices=[
                ('Wheat', 'Wheat'),
                ('Soya hull', 'Soya hull'),
                ('Hay', 'Hay'),
                ('Rice Bran', 'Rice Bran'),
                ('Corn', 'Corn'),
                ('Maize', 'Maize'),
                ('Pellete', 'Pellete'),
            ]),        
        }

class VaccinationForm(forms.ModelForm):
    class Meta:
        model = Vaccination
        exclude = ['cattle']
        widgets = {
            'date_administered': forms.DateInput(attrs={'type': 'date'}),
            'next_due_date': forms.DateInput(attrs={'type': 'date'}),
          }
        
class InsuranceForm(forms.ModelForm):
    class Meta:
        model = Insurance
        exclude = ['cattle']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        if self.instance.pk:  # Check if the instance (contact message) exists
            # Exclude 'name' field from required fields for existing instances
            self.fields['name'].required = False

    class Meta:
        model = ContactMessage  # Replace ContactModel with your actual model name
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.HiddenInput(),  # Hide the name field for authenticated users
            'email': forms.HiddenInput(),  # Hide the email field for authenticated users
        }

from django.contrib.auth.forms import PasswordChangeForm

class SellerPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = SellerEditProfile
        fields = '__all__'

# forms.py
class VetEditProfileForm(forms.ModelForm):
    class Meta:
        model = VetEditProfile
        fields = '__all__'
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'gender': forms.Select(choices=[('---', '---'), ('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')]),
        }
class DeliveryBoyEditProfileForm(forms.ModelForm):
    class Meta:
        model = DeliveryBoyEditProfile
        fields = '__all__'
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'gender': forms.Select(choices=[('---', '---'), ('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')]),
        }

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date','time',  'description', 'veterinarian']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
def clean(self):
        cleaned_data = super(AppointmentForm, self).clean()
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')
        veterinarian = cleaned_data.get('veterinarian')

        if date and time and veterinarian:
            if date < timezone.now().date():
                raise ValidationError("Appointment date must be in the future.")
            if Appointment.objects.filter(date=date, time=time, veterinarian=veterinarian).exists():
                raise ValidationError("Appointment time is already booked. Please choose a different time.")

        return cleaned_data