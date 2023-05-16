from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# from . import forms


# Create your views here.

def home(request):
    return render(request, "authentication/index.html")
def contact(request):
    return render(request, "authentication/contact.html")
def signup(request):
    


    if request.method == "POST":
            
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST['confirmpassword']
        # print(firstname );
            
        myuser = User.objects.create_user(username,email,password)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.save()
        messages.success(request, "Your Account has been Created")


        return redirect('signin')
        
    
        
    return render(request, "authentication/signup.html")
def signin(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username,password);


        user = authenticate(request,username=username, password=password)

        if user is not None:
            
            login(request, user)
            # firstname= User.first_name
            # return render(request, "authentication/dashboard.html", {'firstname':firstname})
            return render(request, "authentication/dashboard.html")
            
        else:
            messages.error(request,"Invalid Username and Password")
            # return redirect('home')    
            # return render(request, "authentication/dashboard.html")

    
    # form = forms.LoginForm()
    # # message = ''
    # if request.method == 'POST':
    #     form = forms.LoginForm(request.POST)
    #     if form.is_valid():
    #         user = authenticate(
    #             username=form.cleaned_data['username'],
    #             password=form.cleaned_data['password'],
    #         )
    #         if user is not None:
    #             login(request, user)
    #             # message = f'Hello {user.username}! You have been logged in'
    #             return render(request, "authentication/dashboard.html")
    #         else:
    #             message = 'Login failed!'
    #             return redirect('home')
    # return render(
    #     request, 'authentication/signin.html')
        





    return render(request, "authentication/signin.html")
def signout(request):
    logout(request)
    messages.success(request,"Logged out Successfully")
    return redirect('home')
    # return redirect('signin')
