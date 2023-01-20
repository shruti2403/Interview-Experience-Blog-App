from django.shortcuts import render
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import OrderForm, CreateUserForm
# from .filters import OrderFilter


# Create your views here.

def front(request):
    # return render(request , 'acc/front.html')
    return HttpResponse('Customer Page')

def registerPage(request):
    form=CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save(  )
    context = {'form':form}
    return render(request, 'acc/register.html',context)

def loginPage(request):
    context = {}
    return render(request, 'acc/login.html')



def new(request):
    return render(request , 'acc/new.html')

# def register(request):
    # return HttpResponse('Customer Page')

def customer(request):
    return render(request, "acc/customer.html")

