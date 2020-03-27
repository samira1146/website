from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import Information, SignUpForm
from .models import Designer,Jornal
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def index(request):
    return HttpResponse("<h1>Hello,This is my app</h1>")

def user_login(request):
    if request.method == 'POST':
        login_form = Information(request.POST)
        if login_form.is_valid():
            username =login_form.cleaned_data.get("username")
            password =login_form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/designer/')
            else:
                error="Please provide the correct password and username"
                login_form = Information()
                return render(request, '1.html', locals())     
    else:
        login_form = Information()
    return render(request, '1.html', locals())

def user_sign_up(request):
    if request.method == 'POST':
        sign_up_form = SignUpForm(request.POST)
        if sign_up_form.is_valid():
            first_name = sign_up_form.cleaned_data.get("first_name")
            last_name = sign_up_form.cleaned_data.get("last_name")
            username = sign_up_form.cleaned_data.get("username")
            password = sign_up_form.cleaned_data.get("password")
            email = sign_up_form.cleaned_data.get("email")
            age = sign_up_form.cleaned_data.get("age")
            work_experience = sign_up_form.cleaned_data.get("work_experience")
            user = User.objects.create(first_name=first_name, last_name=last_name,email=email,username=username)
            user.set_password(password)
            user.save()
            designer = Designer.objects.create(user=user,age=age,work_experience=work_experience)
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/designer/')
            else:
                error="Please provide the correct password and username"
                sign_up_form = SignUpForm()
                return render(request, 'sign_up.html', locals())
    else:
        sign_up_form = SignUpForm()
        return render(request, 'sign_up.html', locals())


    


def user_logout(request):
    logout(request)
    return redirect("/login/")


def designer_list(request):
    if request.user.is_authenticated:
        designer_list=Designer.objects.all()
        return render(request, '2.html',locals())
    else:
        return redirect("/login/")

def jornal_list(request):
    jornal_list=Jornal.objects.all()
    return render(request, '3.html',locals())