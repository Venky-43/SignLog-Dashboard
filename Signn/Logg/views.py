from django.shortcuts import render, redirect
from .forms import SignupForm,LoginForm
from .models import Signup,Login

def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.cleaned_data.pop('confirm_password') 
            form.save()
            return redirect('login')  
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    error = None
    form = LoginForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = Signup.objects.filter(username=username, password=password).first()

            if user:
                if user.user_type == 'Patient':
                    return redirect('patient_dashboard', username=user.username)
                elif user.user_type == 'Doctor':
                    return redirect('doctor_dashboard', username=user.username)
            else:
                error = 'Invalid credentials'

    return render(request, 'login.html', {'form': form, 'error': error})

def patient_dashboard(request, username):
    user = Signup.objects.get(username=username)
    return render(request, 'patient_dashboard.html', {'user': user})

def doctor_dashboard(request, username):
    user = Signup.objects.get(username=username)
    return render(request, 'doctor_dashboard.html', {'user': user})
