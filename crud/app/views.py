from django.shortcuts import render, redirect
from .models import Product
from .forms import Productforms, Signupform
from django.http import HttpResponse

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def ProductView(request):
    if request.method == 'POST':
        prod = Productforms(request.POST)
        if prod.is_valid():
            prod.save()
    prod = Productforms()
    template_name='app/Home.html'
    context = {'prod':prod}
    return render(request, template_name, context)

@login_required(login_url='login')
def SeenView(request):
    prod = Product.objects.all()
    template_name = 'app/seen.html'
    context = {'prod': prod}
    return render(request, template_name, context)

def DelView(request, id):
    if request.method == 'POST':
        de=Product.objects.get(pk=id)
        de.delete()
        return HttpResponse("delete successfully")

def UpdateView(request, id):
    if request.method == 'POST':
        prod = Product.objects.get(pk=id)
        form=Productforms(request.POST, instance=prod)
        if form.is_valid():
            form.save()
            return redirect('seen')
    prod = Product.objects.get(pk=id)
    form=Productforms(instance=prod)
    template_name='app/update.html'
    context = {'form':form }
    return render(request, template_name, context)


def SignupView(request):
    if request.method == 'POST':
        form = Signupform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    form = Signupform()
    template_name = 'app/signup.html'
    context = {'form':form}
    return render(request,template_name,context )


def LoginView(request):
    if request.method == 'POST':

        un = request.POST.get('username')
        pa= request.POST.get('password')

        user = authenticate(username=un, password=pa)
        if user is not None:
            login(request, user)
            return redirect('prodfill')
        else:
            messages.error(request, 'invalid credentials')
    form = AuthenticationForm()
    template_name = 'app/login.html'
    context = {'form':form}
    return render(request, template_name, context)

def logoutView(request):
    logout(request)
    return redirect('login')