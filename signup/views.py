from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import get_user, authenticate
from ECellDjangoProject.settings import EMAIL_HOST_USER
import random

tokens = dict()

# Create your views here.
def signup(request):
    if request.method == "POST":
        # if not username:
        #     otp = random.randint(100000, 999999)
        #     send_mail(
        #         subject="OTP for Django Login",
        #         message="Your OTP is " + str(otp),
        #         from_email=EMAIL_HOST_USER,
        #         recipient_list=[email]
        #     )
        #     tokens[token] = str(otp)
        #     data = {
        #         "otp": otp,
        #         "token": token
        #     }
        #     return render(request, "login.html", data)
        # elif otp_inp:
        #     token_inp = request.POST.get('token')
        #     if tokens[token_inp] == otp_inp:
        #         user = User.objects.create_user(username, email, password)
        #         user.save()
        #     else:
        #         return HttpResponse("Invalid OTP")
        if ('emailid' not in request.session):
            email = request.POST.get("emailid").lower()
            otp = str(random.randint(100000, 999999))
            request.session['verified'] = False
            request.session['otp'] = otp
            request.session['emailid'] = email
            send_mail(
                subject="OTP for Django Login",
                message="Your OTP is " + str(otp),
                from_email=EMAIL_HOST_USER,
                recipient_list=[email]
            )
            data = {
                "emailid": email
            }
            return render(request, "signup.html", data)
        else:
            email = request.POST.get("emailid")
            otp = request.POST.get("otp")
            username = request.POST.get("username")
            password = request.POST.get("password")
            dob = request.POST.get("dob")
            if not username:
                if email == request.session.get("emailid"):
                    if otp == request.session.get("otp"):
                        data = {
                            "verified": True,
                            "email": email
                        }
                        return render(request, "signup.html", data)
                    else:
                        request.session.flush()
                        return HttpResponse("Invalid OTP")
                else:
                    request.session.flush()
                    return HttpResponse("Some Error Occurred")
            else:
                print("Register Process...")
                if request.session.get("emailid") == email:
                    user = User.objects.create_user(username, email, password)
                    user.dob = dob
                    user.save()
                    return HttpResponse("Saved Successfully")
                else:
                    print("Email1: ", email, "Email2: ", request.session.get("emailid"))

    return render(request, "signup.html")

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        print(user)
        if user:
            data = {
                "logged_in": True,
                "user": user
            }
            return render(request, "login.html", data)
        else:
            return HttpResponse("Invalid Credentials")
    user = get_user(request)
    if user.username:
        data = {
            "logged_in": True,
            "user": user
        }
        return render(request, "login.html", data)
    else:
        return render(request, "login.html")