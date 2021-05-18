from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,JsonResponse,FileResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .models import *
from .forms import CreateUserForm
from django.contrib import messages
from .models import User,UserEvents


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,user +' created Account Successfully')
            return redirect('login')


    context = {'form':form}
    return render(request, "register.html",context);


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('userhome')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username = username ,password = password)

            if user is not None:
                login(request,user)
                messages.success(request, username + ' Logged In Successfully')
                return redirect('userhome')
            else:
                messages.info(request , 'Username Or Password is Incorrect')

        context = {}
        return render(request, "login.html",context);



def myaccount(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        mobile = request.POST['mobile']
        address = request.POST['address']

        user = User()
        user.fname = fname
        user.lname = lname
        user.email = email
        user.mobile = mobile
        user.address = address

        user.save()

    return render(request,"myaccount.html")

def bookevent(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        eventname = request.POST.get('eventname', False);
        email = request.POST.get('email', False);
        date = request.POST.get('date', False);
        mobile = request.POST.get('mobile', False);
        altmobile = request.POST.get('altmobile', False);
        amount = request.POST.get('amount',False);
        description = request.POST.get('description', False);
        print(name,eventname)
        eventbook = UserEvents()

        eventbook.name = name
        eventbook.eventname = eventname
        eventbook.email = email
        eventbook.date = date
        eventbook.mobile = mobile
        eventbook.altmobile = altmobile
        eventbook.amount = amount
        eventbook.description = description

        eventbook.save()
        messages.success(request, ' Event Booked Successfully we will Contact You soon through mail Stay Tuned :)')

    return render(request,"bookevent.html")


