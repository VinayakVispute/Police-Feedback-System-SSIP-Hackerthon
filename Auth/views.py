from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import path
from . import views
# Create your views here.

def loginpage(request):
    if 'user' in request.session:
       return redirect('/dashboard/')
    elif request.method == "POST":
        username=request.POST['email']
        pass1 = request.POST['password']
        user = authenticate(request, username = username, password = pass1)
        if user is not None:
            login(request, user)
            fname = user.first_name
            request.session['user'] = username
            request.session['email'] = username
            request.session ['full_name'] = fname;
            messages.success (request, "You are Logged on Successfully !!....")
            return redirect('dashboard/')
        else:
            messages.error(request, "There was an Error ...Kindly Check Your Credentials..")
            return redirect('loginpage') 
    else:
        return render(request, 'Auth/index.html')


def createuser(request):
    if request.method == "POST":
        full_name=request.POST.get('fullname')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        confirm_password = request.POST.get('confirmpass')
        username = request.POST.get('email')
        
        if User.objects.filter(username = username):
            messages.error(request, "User Already Exists !!.... Please Try Again")
            return redirect('loginpage')
        
        if User.objects.filter(email = email):
            messages.error(request, "Email ID  Already Exists !!.... Please Try Again")
            return redirect('loginpage')
        
        
            
        if password != confirm_password :
            messages.error(request, "Password are Not Matching ....So Please Try Again")
            return redirect('loginpage')
            
            
            
        
        
        currUser = User.objects.create_user(username, email, password)
        currUser.first_name = full_name;
        user_details = [full_name, email, ]
        currUser.save();
        messages.success(request, "Your Account is Created Sucessfull ....")
        
        # return path('/dashboard', views.dashboard, name="dashboard") 
        
        
    return render(request, "Auth/signup.html")

def dashboard(request):
    if 'user' in request.session:
        current_user = request.session['user']
        current_user_name = request.session['full_name']
        current_user_email = request.session['email']
        
        param = {'current_user': current_user ,'current_user_name' : current_user_name, 'current_user_email' : current_user_email}
        return render(request, "Auth/dashboard.html", param)
    else:
        return redirect('loginpage')

def logout(request):
    try:
        del request.session['user']
        logout(request)
        messages.success (request, "You are Logged out Successfully !!....")
        
    except:
        return redirect('loginpage')
    return redirect('loginpage')




# def loginpage(request):
#     if request.method == "POST":
#         username = request.POST.get('email')
#         pass1 = request.POST.get('password')
#         user = authenticate(username = username, password = pass1)
#         if user is not None:
            
#             login(request ,user)
#             fname = user.first_name
#             messages.success(request, "Login SucessFully ....")
#             context = {"username" : username, "first_name" : fname, "username" : username, "emailid" : username}
#             return render(request, "dashboard/",context)
#         else:
#             messages.error(request, "Bad Credentials!!!")
#             print("Hell")
#             return redirect('loginpage')
        
        
#     return render(request, "Auth/index.html")