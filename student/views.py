from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
# Create your views here.
def logina(request):
    if request.method=="POST":
        uname=request.POST.get('uname',False)
        pas=request.POST.get('pas',False)
        user=authenticate(username=uname,password=pas)
        if user is not None:
            login(request,user)
            return redirect('main:home')
    return render(request,"student/login.html",{})
def home(request):
    return render(request,"student/home.html")
def acounts(request):
    return render(request,"student/student.html")