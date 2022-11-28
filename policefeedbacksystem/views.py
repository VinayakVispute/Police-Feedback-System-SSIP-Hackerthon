from django.http import HttpRequest
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import path
from . import views
# firebaseConfig={
#     "apiKey": "Use Your Api Key Here",
#     "authDomain": "Use Your authDomain Here",
#     "databaseURL": "Use Your databaseURL Here",
#     "projectId": "Use Your projectId Here",
#     "storageBucket": "Use Your storageBucket Here",
#     "messagingSenderId": "Use Your messagingSenderId Here",
#     "appId": "Use Your appId Here"
# }
# firebase = pyrebase.initialize_app(firebaseConfig)
# authe = firebase.auth()
# database=firebase.database()

# def postsignIn(request):
#     email=request.POST.get('email')
#     pasw=request.POST.get('pass')
#     try:
#         # if there is no error then signin the user with given email and password
#         user=authe.sign_in_with_email_and_password(email,pasw)
#     except:
#         message="Invalid Credentials!!Please ChecK your Data"
#         return render(request,"Login.html",{"message":message})
#     session_id=user['idToken']
#     request.session['uid']=str(session_id)
#     return render(request,"Home.html",{"email":email})

def loginpage(request):
    render(request, "Auth/index.html")
    
def reportpage(request):
    if 'user' in request.session:       
        return render(request, "report.html")
    else:
        return redirect('loginpage')

def generateqrcode(request):
    if 'user' in request.session:       
        return render(request, "generate_qrcode.html")
    else:
        return redirect('loginpage')