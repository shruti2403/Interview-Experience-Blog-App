from django.shortcuts import render,redirect
from django.http import HttpResponse 
from django.contrib.auth.models import User 
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, "Interview_Experience/front.html")

def register(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        ConfirmPassword = request.POST['ConfirmPassword']
        program = request.POST['program']
        grad = request.POST['grad']

        myuser = User.objects.create_user(email,password,program,grad)
        myuser.f_name = fname
        myuser.l_name = lname

        myuser.save()

        messages.success(request, "Your account has successfully been created.")

        return redirect('login')
        
    return render (request, "Interview_Experience/register.html"),