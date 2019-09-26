from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout ,update_session_auth_hash
from django.http import HttpResponse
def Home(request):
	return render(request, 'AllInOne/home.html')
'''
def SignUp(request):
	if request.method == "POST":
		return HttpResponse(html)
		form = UserCreationForm(data = request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'AllInOne/signup.html')
	else:
		form = UserCreationForm()
	return render(request,'AllInOne/signup.html', {'form':form})
'''
'''
def Login(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return redirect('/AllInone/')
	else:
		form = AuthenticationForm()
	return render(request, 'AllInOne/login.html', {'form':form})

def Logout(request):
	if request.method == 'POST':
		logout(request)
		return redirect('/AllInOne/')

@login_required(login_url="/AllInOne/Login/")
def ChangePassword(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)
			return redirect('/AllInOne/')

	else:
		form = PasswordChangeForm(request.user)

	
	return render(request, 'AllInOne/changepassword.html', {'form':form})

# Create your views here.
'''