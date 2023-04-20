from django.shortcuts import render, redirect
from django.contrib import messages
from auth_app.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.

'''Function For Registration Page'''
def authregistration(request):
    
    if request.method == 'POST':
        
        registration_username = request.POST['name']
        registration_email = request.POST['email']
        registration_password = request.POST['password']
        registration_confirm_password = request.POST['confirm_password']
        
        '''Check if password confirm_password are matches'''
        if registration_password == registration_confirm_password:
            
            if User.objects.filter(username=registration_username).exists():
                messages.error(request, 'Username Already Exists')
                
            elif User.objects.filter(email=registration_email).exists():
                messages.error(request, 'Email Already Exists')
                
            # Using User.objects.create_user user will be created is admin database
            else:
                registration_user = User.objects.create_user(username=registration_username,  email=registration_email, password = registration_password)
                registration_user.save()
                messages.success(request, 'You have Successfully Registered')
                return redirect("login")
            
        else:
            messages.error(request, 'Password and Conform Password Not Matched')            

    return render(request, 'auth_app/registration.html')


'''Function For Login Page'''
def authlogin(request):
    
    if request.method == 'POST':
        login_email = request.POST['email']
        login_password = request.POST['password']
        
        '''authenticate will check for correct email and password'''
        auth_user = authenticate(request, email=login_email, password=login_password)

        if auth_user is not None:
            login(request, auth_user)
            return redirect("quiz_app:profile")
        
        # To display error message for invalid Email or Password
        else:
            messages.error(request, 'Email or Password Invalid !')
        
    return render(request, 'auth_app/login.html')



'''Function For Logout Page'''
def authlogout(request):
    logout(request)
    messages.success(request, 'Logout Successfully')
    return redirect('login')
