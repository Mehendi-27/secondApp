from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login,authenticate

# Create your views here.

def logIn(request):

    if request.method=="POST":
        username=request.POST.get('user')
        passwd=request.POST.get('pass')
        user=authenticate(request,username=username,password=passwd)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Authentication Failed <a href='/login/'>Go Back</a>")

    context={
        'page':'Login'
    }
    return render(request,'login.html',context)
