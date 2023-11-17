from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django_countries.widgets import CountrySelectWidget
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django_countries.fields import CountryField
from .models import Member, Donor, Project, Payment, DonorNiya
from django.forms import ModelForm
from django.utils import timezone
from datetime import datetime
from datetime import date


DCHOICE = (
    ("Iftaresaim", "Iftaresaim"),
    ("Ouduhuya", "Ouduhuya"),
    ("Mesjid", "Mesjid"),
    ("Quran", "Quran"),
    ("ZekatelFiter", "ZekatelFiter"),
    ("Mesakin", "Mesakin"),
    ("Education", "Education"),)


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class MemberForm(ModelForm):
    Phone_number = PhoneNumberField(widget=PhoneNumberPrefixWidget(initial='ET'), required=False)
    class Meta:
        model = Member
        fields = '__all__'
        exclude = ['MID']

        MID = forms.CharField(help_text="Your Member ID is Generated no need to add")
        Fullname = forms.CharField(widget=forms.TextInput({'class': 'form-control mt-2'}))
        Phone_number = PhoneNumberField(widget=PhoneNumberPrefixWidget(initial="ET"))
        Phone_number.error_messages['invalid'] = 'Incorrect International Calling Code or Mobile Number!'
        Country = CountryField().formfield()
        Email = forms.CharField(widget=forms.TextInput({'class': 'form-control mt-2'}))
        Joined_date = forms.DateField(widget=forms.TextInput({'class': 'form-control mt-2'}))

        labels = {
            'MID': 'Members ID number',
            'Fullname': 'Full Name',
            'Phone_number': 'Phone Number',
            'Country': 'Country',
            'Email': 'Email',
            'Joined_date': 'Joined_date'
        }

    def __init__(self, *args, **kwargs):
        super(MemberForm, self).__init__(*args, **kwargs)
        #self.fields['MID'].required = False
        self.fields['Fullname'].required = True
        self.fields['Country'].empty_label = "Select"
        #self.fields['Phone_number'].required = True


class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'

        #DMID = forms.ModelChoiceField(queryset=Payment.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
        DMID = forms.CharField(widget=forms.TextInput({'class': 'form-control mt-2'}))
        Fullname = forms.ModelChoiceField(queryset=Payment.objects.all(),
                                          widget=forms.Select(attrs={'class': 'form-control'}))
        Year = forms.ChoiceField()
        January = forms.CharField(widget=forms.TextInput({'class': 'form-control mt-2'}))
        February = forms.CharField(widget=forms.TextInput({'class': 'form-control mt-2'}))
        March = forms.CharField(widget=forms.TextInput({'class': 'form-control mt-2'}))
        April = forms.CharField(widget=forms.TextInput({'class': 'form-control mt-2'}))
        May = forms.CharField(widget=forms.TextInput({'class': 'form-control mt-2'}))
        June = forms.CharField(widget=forms.TextInput({'class': 'form-control mt-2'}))
        July = forms.CharField(widget=forms.TextInput({'class': 'form-control mt-2'}))
        August = forms.CharField(widget=forms.TextInput({'class': 'form-control mt-2'}))
        September = forms.CharField(widget=forms.TextInput({'class': 'form-control mt-2'}))
        October = forms.CharField(widget=forms.TextInput({'class': 'form-control mt-2'}))
        November = forms.CharField(widget=forms.TextInput({'class': 'form-control mt-2'}))
        December = forms.CharField(widget=forms.TextInput({'class': 'form-control mt-2'}))
        Total = forms.CharField(widget=forms.TextInput({'class': 'form-control mt-2'}))

        labels = {
            'DMID': 'Member ID Number',
            'Fullname': 'Full Name',
            'Year': 'Year',
            'January': 'January',
            'February': 'February',
            'March': 'March',
            'April': 'April',
            'May': 'May',
            'June': 'June',
            'July': 'July',
            'August': 'August',
            'September': 'September',
            'October': 'October',
            'November': 'November',
            'December': 'December',
            'Total': 'Total'
        }

    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)
        self.fields['DMID'].required = True
        self.fields['Fullname'].required = True


class DonorForm(ModelForm):
    Phone_number = PhoneNumberField(widget=PhoneNumberPrefixWidget(initial='ET'), required=False)
    class Meta:
        model = Donor
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super(DonorForm, self).__init__(*args, **kwargs)
        self.fields['Fullname'].required = True
        self.fields['Donation_attachment'].required = False

class DonorNiyaForm(ModelForm):
    Phone_number = PhoneNumberField(widget=PhoneNumberPrefixWidget(initial='ET'), required=False)
    class Meta:
        model = DonorNiya
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super(DonorNiyaForm, self).__init__(*args, **kwargs)
        self.fields['Fullname'].required = True
        
