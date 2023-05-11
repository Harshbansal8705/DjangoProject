from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request, "authentication/index.html")
def signup(request):
    try:


        if request.method == "POST":
            
            name = request.POST.get('name')
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            email = request.POST.get('email')
            password = request.POST.get('password')
            # confirmpassword = request.POST['confirmpassword']
            # print(firstname );
            
            # myuser = User.objects.create_user(name,email,password)
            # myuser.first_name = firstname
            # myuser.last_name = lastname
            # myuser.save()
            # messages.success(request, "Your Account has been Created")


            return redirect('signin')
        
    except:
        pass
        
    return render(request, "authentication/signup.html")
def signin(request):
    return render(request, "authentication/signin.html")
def signout(request):
    pass
