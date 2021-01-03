from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def support(request):
    return render(request,'support.html')

def login(request):
    return render(request,'user/login.html')

def signup(request):
    return render(request,'user/signup.html')

def forgotPassword(request):
    return render(request,'user/forgotPassword.html')

def dashboard(request):
    return render(request,'user/dashboard/index.html')

# def ChangePassword(request):
#     return render(request,'user/dashboard/changePassword.html')

