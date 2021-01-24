from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import CreateUserForm

def registerPage(request):
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)
			return redirect('login')

		else:
			form = CreateUserForm(request.POST)
			context = {'form': form}
			return render(request, 'accounts/register.html',context)

def loginPage(request):
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')
		else:
			context = {}
			return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')


def home(request):
	return render(request,'accounts/home.html')

def contact(request):
	return render(request,'accounts/contact.html')

def cost(request):
		if request.method=='post':
			return render(request,'account/cart.html')

		else:
			return HttpResponse(request,'accounts/cost.html')

def cart(request):
	return redirect(request,'accounts/cart.html')