from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth,messages

def Signup(request):
    if request.method == 'POST':
        if request.POST['p1']==request.POST['p2']:
            try:
                user=User.objects.get(username=request.POST['username'])
                email1=User.objects.get(email=request.POST['email'])
                print('see down \n')
                print(user)
                print(email1)
                if user :
                    messages.error(request,'Username already exists')
                    return redirect('home')
                if email1 :
                    messages.error(request,'Email already exists')
                    return redirect('home')
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'],
                                                email=request.POST['email'],password=request.POST['p1'])
                auth.login(request,user)
                return redirect('home')
        else:
            messages.error(request,'password did not match')
            return redirect('home')


def Login(request):
    if request.method == 'POST':
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')

        else:
            messages.error(request,'username or password is incorrect!')
            return redirect('home')



def Logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
