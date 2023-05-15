from random import randint

from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from twilio.rest import Client

from apps.forms import RegisterForm
from apps.models import User


# Create your views here.


def register_view(request):
    if request.method == 'POST':
        forms = RegisterForm(data=request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('login_view')
        else:
            print(forms.errors)
    return render(request, 'auth/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user:
            user.confirm = randint(10000,100000)
            user.save()
            account_sid = 'AC45bf978b56ceb8228d18b32e5736d6cb'
            auth_token = '5b14e6fa667d096d4131d092b7f4ca24'
            client = Client(account_sid,auth_token)

            message = client.messages.create(
                to=user.phone,
                from_='+12542806001',
                body=f'your confirmation code is {user.confirm}'
            )
            return redirect('confirmation_code',user.id)

        else:
            redirect('/login')
    return render(request, 'auth/login.html')

def confirm(request,id):
    if not request.user.is_authenticated:
        user = User.objects.get(id=id)
        print(user.username)
        if user and user.confirm != None:
            if request.method == 'POST':
                confirm = request.POST['confirmation_code']
                if user.confirm == int(confirm):
                    login(request,user)
                    user.confirm = None
                    user.save()
                    return redirect('/')
                else:
                    print('error')
        else:
            redirect('/')
    else:
        redirect('/')
    return render(request, 'auth/confirm.html', {'user': user,'user_phone': user.phone[-2:] })

def home_page(request):
    return render(request, 'home.html')
