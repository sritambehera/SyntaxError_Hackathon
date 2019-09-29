from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .forms import BranchForm, SemesterForm, MaterialForm
from .models import Branch , Semester, Material

@login_required(login_url="/AllInOne/Login/")
def Upload(request):
	if request.method == 'POST':

		a = BranchForm(request.POST)
		b = SemesterForm(request.POST)
		c = MaterialForm(request.POST, request.FILES)
		a_valid = a.is_valid()
		b_valid = b.is_valid()
		c_valid = c.is_valid()
		if a_valid and b_valid and c_valid:
			a.save()
			b.save()
			c.save()
		return redirect('/AllInOne')
	else:
		a = BranchForm()
		b = SemesterForm()
		c = MaterialForm()
	return render(request, 'AllInOne/upload.html', {'a': a, 'b' : b , 'c': c})




def Home(request):
	return render(request, 'AllInOne/home.html', )

def SignUp(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'AllInOne/home.html')
	else:
		form = UserCreationForm()
	return render(request, 'AllInOne/signup.html', {'form': form})

def Login(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return redirect('/AllInOne/')
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
