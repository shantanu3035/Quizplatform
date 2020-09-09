
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserRegisterForm
from django.contrib import messages
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from profiles.forms import StudentProfileUpdateForm, TeacherProfileUpdateForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        u_form = CustomUserRegisterForm(request.POST)
        if u_form.is_valid():
            u_form.save()
            email = u_form.cleaned_data.get("email")
            user_type = u_form.cleaned_data.get("user_type")
            messages.success(request, f'User created for {email}, you can now log in!')
            return redirect('login')
    else:
        u_form = CustomUserRegisterForm(request.POST)
        return render(request, "users/register.html", {'u_form':u_form})

@login_required
def dashboard(request):  
    if request.user.user_type == 'ST':
        return redirect('quizes')
       # return HttpResponse("You are redirected to the student dashboard for your user") #Open the quiz list view dashboard
    elif request.user.user_type == 'TE':
        return redirect('quizes')  #Open the current student's dashboard
    else:
        return HttpResponse("You can now login through the admin page")


@login_required
def profile(request):
    if request.method == 'POST':
        if request.user.user_type == 'ST':
            p_form = StudentProfileUpdateForm(request.POST, instance=request.user.profile)  #For student make roll number visible
        else:
            p_form = TeacherProfileUpdateForm(request.POST, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Profile details updated')
            return redirect('profile') #Enter path to user profile here
    else:
        if request.user.user_type == 'ST':
            p_form = StudentProfileUpdateForm(instance=request.user.profile)
        else:
            p_form = TeacherProfileUpdateForm(instance=request.user.profile)
        return render(request, "users/profile.html", {'p_form':p_form}) #Enter path here
