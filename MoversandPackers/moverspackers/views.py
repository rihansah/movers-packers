from asyncio import start_server
from distutils.log import error
from math import remainder
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, logout,login


# Create your views here.
from .models import *
from datetime import date
def index(request):
    return render(request, 'index.html')


def admin_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['pwd']
        user = authenticate(username=u, password= p)
        try:
            if user.is_staff:
                login(request,user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request, 'admin_login.html', locals())

def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request, 'admin_home.html')

def Logout(request):
    logout(request)
    return redirect(index)

def add_services(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    if request.method =="POST":
        st= request.POST['servicetitle']
        des= request.POST['description']
        image= request.FILES['image']
        try:
            Services.objects.create(title=st,description=des, image=image)
            error="no"
        except:
            error="yes"
    
    return render(request, 'add_services.html',locals())

def manage_services(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    services = Services.objects.all()
    
    return render(request, 'manage_services.html',locals())


def edit_service(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    service = Services.objects.get(id=pid)
    error = ""
    if request.method =="POST":
        st= request.POST['servicetitle']
        des= request.POST['description']

        service.title = st
        service.description = des

        try:
            service.save()
            error="no"
        except:
            error="yes"
        
        try:
            image= request.FILES['image']
            service.image = image
            service.save()
        except:
            pass

    return render(request, 'edit_service.html',locals())

def delete_service(request,pid) :
    service=Services.objects.get(id=pid)
    service.delete()
    return redirect('manage_services')

def services(request):
    services = Services.objects.all()
    return render(request, 'services.html',locals())


def about(request):
    return render(request, 'about.html')

def request_quote(request):
    error = ""
    if request.method =="POST":
        name= request.POST['name']
        email= request.POST['email']
        contact= request.POST['contact']
        location= request.POST['location']
        shiftingloc = request.POST['shiftingloc']
        shiftingdate= request.POST['shiftingdate']
        briefitems= request.POST['briefitems']
        items= request.POST['items']
        
        try:
            SiteUser.objects.create(name=name,email=email, mobile=contact, location=location, shiftingloc=shiftingloc, shiftingdate=shiftingdate, briefitems=briefitems, items=items, requestdate=date.today())
            error="no"
        except:
            error="yes"
    
    return render(request, 'request_quote.html',locals())


def new_booking(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    booking = SiteUser.objects.filter(status=None)
    
    return render(request, 'new_booking.html',locals())

def view_bookingdetail(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    booking = SiteUser.objects.get(id=pid)
    if request.method =="POST":
        remark= request.POST['remark']
        try:
            booking.remark = remark
            booking.status = "1" 
            booking.updationdate = date.today()
            booking.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'view_bookingdetail.html',locals())

def old_booking(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    booking = SiteUser.objects.filter(status="1")
    
    return render(request, 'old_booking.html',locals())

def delete_booking(request,pid) :
    booking=SiteUser.objects.get(id=pid)
    booking.delete()
    return redirect('old_booking')