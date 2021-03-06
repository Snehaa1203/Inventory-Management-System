
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm,UserUpdateForm,ProfileUpdateForm
from .models import Profile

def register(request):
	if request.method == 'POST':
	 form=CreateUserForm(request.POST)
	 if form.is_valid():
		 form.save()
		 return redirect('login')
	else:
		 form=CreateUserForm()

	context={'form':form}
	return render(request,'register.html',context)

def profile(request):
	return render(request,'profile.html')

def profile_update(request):
	profile = Profile.objects.get_or_create(staff=request.user)
		  
	if request.method == 'POST':
			user_form=UserUpdateForm(request.POST,instance=request.user)
			profile_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
			if user_form.is_valid()and profile_form.is_valid:
				user_form.save()
				profile_form.save()
				return redirect('profile')
	else:
			user_form=UserUpdateForm(instance=request.user)
			profile_form=ProfileUpdateForm(instance=request.user.profile)

	context={'user_form':user_form,'profile_form':profile_form}
	return render(request,'profile_update.html',context)
