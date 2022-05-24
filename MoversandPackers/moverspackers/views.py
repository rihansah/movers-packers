from distutils.log import error
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, logout,login


# Create your views here.
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
    return render(request, 'add_services.html')