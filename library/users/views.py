
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from users.models import Users


def register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        c=request.POST['c']
        f=request.POST['f']
        l=request.POST['l']
        e=request.POST['e']

        if(p==c):
            u=User.objects.create_user(username=u,password=p,first_name=f,last_name=l,email=e)
            u.save()
        else:
            return HttpResponse("password are not matching")
        return redirect('users:login')
    return render(request,'adminregister.html')



def user_login(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
        else:
            return HttpResponse("invalid user")
        return redirect('books:home')





    return render(request, 'login.html')




def view_users(request):
    k=User.objects.all()       #reads all records from the table named book
    return render(request,'view_users.html',{'user':k})

def user_logout(request):
    logout(request)
    return redirect('users:login')

