from django.shortcuts import render,redirect
from .models import *
from django.core.paginator import Paginator
# Create your views here.
def login(request):
    return render(request,"adminss/login.html",{})
def home(request):
    return render(request,"admins/home.html")
def acounts(request):
    if request.method=="POST":
        grad=request.POST.get('grade',False)
        sece=request.POST.get('sec',False)
        sec=Section(grade=grad,section=sece)
        
        sec.save()

        return redirect('main:acounts')
    sb=Section.objects.filter()
    pag=Paginator(sb,2)
    page=request.GET.get("page")
   
    page_obj=pag.get_page(page)
    return render(request,"admins/acounts.html",{'page_obj':page_obj})
def view_student(request,id):
    if request.method=='POST':
        uname=request.POST.get('uname',False)
        fname=request.POST.get('fname',False)
        lname=request.POST.get('lname',False)
        age=request.POST.get('age',False)
        role=request.POST.get('role',False)
        gender=request.POST.get('gender',False)
        image=request.POST.get('image',False)
        se=Section.objects.get(id=id)
        user=Account(sec=se,uname=uname,fname=fname,lname=lname,age=age,role=role,image=image,gender=gender)
        user.save()
        se=Section.objects.get(id=id)
        user=Account.objects.filter(sec=se)
        paginator=Paginator(user,1)
        page_number=request.GET.get("page")
        page_obj=paginator.get_page(page_number)
        return render(request,"admins/view_student.html",{'page_obj':page_obj})
    se=Section.objects.get(id=id)
    user=Account.objects.filter(sec=se)
    paginator=Paginator(user,1)
    page_number=request.GET.get("page")
    page_obj=paginator.get_page(page_number)
    return render(request,"admins/view_student.html",{'page_obj':page_obj,'sec':se})


    """if request.method=='POST':
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
    paginator=Paginator(user,1)
    page_number=request.GET.get("page")
    page_obj=paginator.get_page(page_number)
    teacher=Account.objects.filter(role=2)
    dir=Account.objects.filter(role=3)
    head=Account.objects.filter(role=4)
    return render(request,"admins/acounts.html",{'page_obj':page_obj,'teach':teacher,'dir':dir,'head':head})"""
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
    if request.method=="POST":
        streem=request.POST.get('streem',False)
        nsub=request.POST.get('name',False)
        descr=request.POST.get('grade',False)
        st=Streem(streem=streem,name=nsub,grade=descr)
        st.save()
    user=Streem.objects.all()
    
    return render(request,"admins/departiment.html",{'user':user})