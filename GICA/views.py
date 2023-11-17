from django.shortcuts import  render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django import forms
from .forms import MemberForm, DonorForm, PaymentForm, NewUserForm, DonorNiyaForm
from .models import Member, Donor, Project, IslamicEvent, Payment, New, DonorNiya
from django.conf.urls.static import static
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate #add this
from django.template import loader
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
import random, string
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
posts = [
    {
        'author': 'Admin',
        'title': 'Post 1',
        'content': 'First post content',
        'date_posted': 'July 7, 2023'
    },
    {
        'author': 'Admin',
        'title': 'Post 2',
        'content': 'Second post content',
        'date_posted': 'July 10, 2023'
    }
]

def handle_uploaded_file(f):  
    with open(f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk) 
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="GICA/register_new.html", context={"register_form":form})
def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("main:homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="GICA/login.html", context={"login_form":form})
def list(request):
    context = {'list': Member.objects.all()}
    return render(request, "GICA/list.html", context)

def register(request, pk=0):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            m = form.save(commit=False)
            m.MID = request.POST.get('MID', False)
            m.Fullname = form.cleaned_data['Fullname']
            #m.Phone_number='Phone_number'
            m.Country = request.POST.get('Country', False)
            m.Email = request.POST.get('Email', False)
            m.save()
            messages.success(request, 'You are registered successfully. Your Member ID is also Generated')
            return render(request, "GICA/register.html", {'form': MemberForm(request.GET)})
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)
    else:
        form = MemberForm()

    return render(request, 'GICA/register.html', {'form': form})
             
        
##def donate(request, pk=0):
##    if request.method == "GET":
##        if pk == 0:
##            form = DonorForm()
##        else:
##            donor = Donor.objects.get(pk=pk)
##            form = DonorForm(instance=donor)
##        return render(request, "GICA/donate.html", {'form': form})
##    else:
##        if pk == 0:
##            form = DonorForm(request.POST)
##        else:
##            donor = Donor.objects.get(pk=pk)
##            form = forms.DonorForm(request.POST, request.FILES, instance= donor)
##        if form.is_valid():
##            newUser2=Donor(
##                 Fullname = request.POST.get('Fullname', False),
##                 Amount = request.POST.get('Amount', False),
##                 Donation_type = request.POST.get('Donation_type', False),
##                 Donation_attachment = request.POST.get('Donation_attachment', False),
##                 upload_finished_at = request.POST.get('upload_finished_at', False)
##                )
##            newUser2.save()
##            messages.success(request, 'Yoour donation is registered successfully.')
##            return render(request, "GICA/donate.html", {'form': form})
##        else:
##            messages.error(request, 'Invalid form submission.')
##            messages.error(request, form.errors)

def donate(request):
    if request.method == "POST":
        form = DonorForm(request.POST, request.FILES)
        if form.is_valid():
            d=form.save(commit=False)
            d.Fullname = request.POST.get('Fullname', False)
            d.Country = request.POST.get('Country', False)
            d.Amount = request.POST.get('Amount', False)
            d.Donation_type = request.POST.get('Donation_type', False)
            d.Donation_attachment=request.FILES["Donation_attachment"]
            d.upload_finished_at = request.POST.get('upload_finished_at', False)
            d.save()
            messages.success(request, 'Yoour donation is registered successfully.')
            return render(request, "GICA/donate.html", {'form': form})
    else:
        form = DonorForm()
    return render(request, "GICA/donate.html", {"form": form})

def donateniya(request):
    if request.method == "POST":
        form = DonorNiyaForm(request.POST)
        if form.is_valid():
            f= form.save(commit=False)
            f.Fullname = request.POST.get('Fullname', False)
            f.Amount = request.POST.get('Amount', False)
            f.Donation_type = request.POST.get('Donation_type', False)
            #f.Phone_number='+251913677468'
            f.Country = request.POST.get('Country', False)
            f.save()
            messages.success(request, 'Yoour donation Niya is registered successfully.')
            return render(request, "GICA/donateniya.html", {'form': form})
    else:
        form = DonorNiyaForm()
    return render(request, "GICA/donateniya.html", {"form": form})



class payment_list(ListView):
    template_name = 'GICA/allpayment.html'
    model = Payment
    context_object_name = "payments"
    
class allproject(TemplateView):
    template_name = 'GICA/project1.html'

    def get_context_data(self, **kwargs):
        context = super(allproject, self).get_context_data(**kwargs)
        projects = Project.objects.all()
        context.update({'projects': projects})
        return context
class members_list(ListView):
    template_name = 'GICA/memberslist.html'
    model = Member
    context_object_name="members"

class events_list(ListView):
    template_name = 'GICA/islamicevents.html'
    model = IslamicEvent
    context_object_name="islamicevents"
    
class news_list(ListView):
    template_name = 'GICA/news.html'
    model = New
    context_object_name="news" 

def employee_delete(request,id):
    employee = Member.objects.get(pk=id)
    employee.delete()
    return redirect('GICA/register.html')

def index(request):
    context = {
        'posts': New.objects.all()
    }
    return render(request, 'GICA/home.html', context)

def base(request):
   return render(request, 'GICA/base.html', {'title': 'Base'})   
def about(request):
    return render(request, 'GICA/about.html', {'title': 'About Us'})
def project(request):
    return render(request, 'GICA/project.html', {'title': 'Projects'})

def project2(request):
    return render(request, 'GICA/project2.html', {'title': 'Support'})        
def project3(request):
    return render(request, 'GICA/project3.html', {'title': 'Employment Oportunity'})
def project4(request):
    return render(request, 'GICA/project4.html', {'title': 'Islamic Institutions'})
def news(request):
    context = {
        'posts': New.objects.all()
    }
    return render(request, 'GICA/news.html',context)    
def contact(request):
    return render(request, 'GICA/contact.html', {'title': 'Contact Us'})
