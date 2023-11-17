from django.db import models
from .forms import MemberForm,DonorForm
from django.contrib import admin
#from .reports import Paymentreport
from .models import Member, Donor, Project, IslamicEvent, Payment, New, DonorNiya



class AdminMember(admin.ModelAdmin):
    
    model = Member
    list_display = ('MID', 'Fullname', 'Phone_number', 'Country', 'Email', 'Joined_date')

class AdminDonor(admin.ModelAdmin):
    model = Donor
    list_display = ('Fullname', 'Amount', 'Phone_number', 'Country', 'Donation_type', 'Donation_attachment')

class AdminDonorNiya(admin.ModelAdmin):
    model = DonorNiya
    list_display = ('Fullname', 'Amount', 'Donation_type', 'Phone_number', 'Country')

class AdminPayment(admin.ModelAdmin):
    model = Payment
    list_filter = ('DMID', 'Fullname','Year', 'Total')
    list_display = ('DMID', 'Fullname','Year', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
                    'December', 'Total')
    
#reports.register(Payment, Paymentreport)    

admin.site.register(Member, AdminMember)
admin.site.register(Donor, AdminDonor)
admin.site.register(DonorNiya, AdminDonorNiya)
admin.site.register(Project)
admin.site.register(IslamicEvent)
admin.site.register(Payment, AdminPayment)
admin.site.register(New)

# Register your models here.
