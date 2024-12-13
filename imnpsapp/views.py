# from django.shortcuts import render,redirect
# from .models import imnps
# from .forms import *
# from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages

# @login_required
# def nos(request):
#     safa=imnps.objects.all()
#     return render(request,'index.html',{'safa':safa})

# # def ipls(request):
# #     if request.method=='POST':
# #         form=ngl(request.POST)
# #         if form.is_valid():
# #             form.save()
# #             return redirect('safa')
        
# #         else:
# #             form=ngl()
# #             #safa=imnps.objects.all()

# #     return render(request,'form.html',{'form':form})


# def ipls(request):
#     form = ngl()  
    
#     if request.method == 'POST':
#         form = ngl(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('safa')

#     return render(request, 'form.html', {'form': form})


# # def login(request):
# #     if request.method=='POST':
# #         username=request.POST.get('username')
# #         password=request.POST.get('password')
# #         user=authenticate(request,username=username,password=password)
# #         if user is not None:
# #             login(request,user)
# #             return redirect('safa')
# #         else:
# #             messages.error(request,'invalid username')
# #     return render(request,'login.html')

# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('safa')  # Adjust according to your view name
#         else:
#             messages.error(request, 'Invalid username or password')
#     return render(request, 'login.html')




# def logout(request):
#     logout(request)
#     return redirect('login')  




from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail


# Login view
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the homepage after successful login
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'login.html')

# Logout view
def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logging out

# Home view (protected by login_required)
@login_required
def home(request):
    # The homepage (index.html) should only be accessible after login
    return render(request, 'index.html')




def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Create the user
            messages.success(request, 'Your account has been created successfully! You can now log in.')
            return redirect('login')  # Redirect to the login page after successful registration
        else:
            messages.error(request, 'There was an error with your registration. Please try again.')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'register.html', {'form': form})



def set_session(request):
    request.session['username']='JohnDoe'
    return render(request,'set_session.html')

def get_session(request):
    username=request.session.get('username','Guest')
    return render (request,'get_session.html',{'username':username})


def delete_session(request):
    try:
        del request.session['username']
    except KeyError:
        pass
    return render(request,'delete_session.html')


def set_cookie(request):
    response=render(request,'set_cookie.html')
    response.set_cookie('user_preference','dark_mode',max_age=3600)
    return response


def get_cookie(request):
    preference=request.COOKIES.get('user_preference', 'light_mode')
    return render(request,'get_cookie.html', {'preference': preference})


def delete_cookie(request):
    response=render(request, 'delete_cookie.html')
    response.delete_cookie('user_preference')
    return response



def send_email_view(request):
    send_mail(
        'Welcome to Django Email',
        'This email confirms the setup of your email functionality in Django.',
        'sf3027574@gmail.com',  
        ['joelscaria2002@gmail.com'],  
        fail_silently=False,
    )
    return HttpResponse('Email sent successfully!')