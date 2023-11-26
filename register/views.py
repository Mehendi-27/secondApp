from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.

def register(request):
    if request.method=="POST":
        user=request.POST.get('name')
        email=request.POST.get('email')
        passwd=request.POST.get('pass')
        newUser=User.objects.create_user(user,email,passwd)
        newUser.save()
        return HttpResponse("Registration Succesfull  <a href='/login/'>Log In</a>")

    context={
        'page':'Register'
    }
    return render(request,'register.html',context)