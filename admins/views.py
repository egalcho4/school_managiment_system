from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def login(request):
    return render(request,"adminss/login.html",{})
def home(request):
    return render(request,"admins/home.html")
def acounts(request):
    if request.method=='POST':
        uname=request.POST.get('uname',False)
        fname=request.POST.get('fname',False)
        lname=request.POST.get('lname',False)
        age=request.POST.get('age',False)
        role=request.POST.get('role',False)
        gender=request.POST.get('gender',False)
        image=request.POST.get('image',False)
        user=Account(uname=uname,fname=fname,lname=lname,age=age,role=role,image=image,gender=gender)
        user.save()
        return redirect('main:acounts')

    user=Account.objects.filter(role=1)
    teacher=Account.objects.filter(role=2)
    dir=Account.objects.filter(role=3)
    head=Account.objects.filter(role=4)
    return render(request,"admins/acounts.html",{'user':user,'teach':teacher,'dir':dir,'head':head})
def update_users(request,id):
    user=Account.objects.get(id=id)
    if request.method=='POST':
        uname=request.POST.get('uname',False)
        fname=request.POST.get('fname',False)
        lname=request.POST.get('lname',False)
        age=request.POST.get('age',False)
        role=request.POST.get('role',False)
        gender=request.POST.get('gender',False)
        image=request.POST.get('image',False)
        user.uname=uname
        user.fname=fname
        user.lname=lname
        user.age=age
        user.role=role
        user.gender=gender
        user.image=image
        user.save()
        return redirect('main:acounts')
    return render(request,"admins/update_user.html",{'user':user})
def delete_users(request,id):
    user=Account.objects.get(id=id)
    user.delete()
    return redirect('main:acounts')
def departiment(request):
    return render(request,"admins/departiment.html")