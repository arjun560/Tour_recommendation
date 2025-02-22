from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def fyp(request):
    return render(request,'fyp.html')

def service(request):
    return render(request,'service.html')

def login(request):
    return render(request,'login.html')

def recomendations(request):
    return render(request,'recomendations.html')

def contact(request):
    return render(request,'contact.html')

def userdash(request):
    return render(request,'userdash.html')

def favlocation(request):
    return render(request,'favlocation.html')

def recentrecom(request):
    return render(request,'recentrecom.html')

def support(request):
    return render(request,'support.html')

def testimonial(request):
    return render(request,'testimonial.html')

def profile(request):
    return render(request,'profile.html')