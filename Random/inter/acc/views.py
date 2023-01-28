from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import  CreateUserForm
# from .filters import OrderFilter


# Create your views here.

def front(request):
    return render(request , 'acc/front.html')
    # return HttpResponse('Front Page')

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for' + user )
            return redirect('login')
    context = {'form':form}
    return render(request, 'acc/register.html',context)
# 
def loginPage(request):
    # context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password = password)

        if user is not None:
            login(request , user)
            return redirect('cust')
    return render(request, 'acc/login.html')



def new(request):
    return render(request , 'acc/new.html')

# def register(request):
    # return HttpResponse('Customer Page')

# def customerr(request):
    # customers = customer.objects.all()
    # company = customer_comp.objects.all()
    # jobtype = Job_type.objects.all()
    # jobprofile = job_profile.objects.all()
    # data = {'customers' : customers , 'comp' : company, 'jobT' : jobtype , 'jobP': jobprofile}
    # return render(request, "acc/customer.html", data)

def main_customers(request):
    # cust = main_customer.objects.get(id = pk_test)
    customers = main_customer.objects.all()
    context = {'customers':customers}
    return render (request, 'acc/customer.html',context)

def jobtype(request):
    jobtypes = Job_type.objects.all()
    data = {'jobtype':jobtypes}
    render(request, 'acc/customer.html',data)

