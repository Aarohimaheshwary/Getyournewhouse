from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import product, Contact, profile,newss


def index(request):
    a = product.objects.all()
    return render(request, 'index.html', {'a': a})


def about(request):
    x = profile.objects.all()
    return render(request, 'about-us.html', {'x': x})


def registration(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken")
                return redirect('/registration')
            elif User.objects.filter(email=email).exists():
                return HttpResponse('email taken')
                return redirect('/registration')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name, last_name=last_name)
                user.save()
                print('user created')
                return redirect('/login')
        else:
            messages.info(request, 'password not matching...')
            return redirect('/registration')
        return redirect('/')
    else:
        return render(request, 'registration.html')


def news(request):
    g = newss.objects.all()
    return render(request, 'news.html',{'g': g})


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", '')
        email = request.POST.get("email", '')
        phone = request.POST.get("phone", '')
        desc = request.POST.get("desc", '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        return HttpResponse("conatct saved in database")
        return redirect('/contact')
    return render(request, 'contact.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'invalid credentials')
            return redirect('/login')
        return render(request,'index.html')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')