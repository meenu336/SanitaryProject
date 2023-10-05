from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .models import CustomUser  # Assuming you have a CustomUser model
# Create your views here.

def index(request):
    return render(request,'index.html')

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('index')

def registration(request):
     if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']  # Make sure this matches your form field name
        #user_type = request.POST['user_type']

        if password != confirm_password:
            # Handle password mismatch error
            return render(request, 'registration.html', {'error_message': 'Passwords do not match'})

        # Create a new user object
        user = CustomUser.objects.create_user(username=username, email=email, password=password)
        # You may want to do additional processing here if needed

        return redirect('login')  # Redirect to login page after successful registration

     return render(request,'registration.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        # if user is not None:
        #     login(request, user)
        #     return redirect('dashboard')
        # else:
        #     return render(request, 'login.html', {'error_message': 'Invalid username or password'})

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Check if username exists in the database
            if not CustomUser.objects.filter(username=username).exists():
                error_message = 'Wrong username'
            else:
                error_message = 'Wrong password'

            return render(request, 'login.html', {'error_message': error_message})


    return render(request,'login.html')

@login_required(login_url='login')
def home(request):
    return render(request,'home.html')