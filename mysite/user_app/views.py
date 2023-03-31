from django.contrib import messages
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from . forms import CreateUser
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
import random
from django.urls import reverse_lazy, reverse
from .models import PreRegistration
from .forms import VerifyForm,LoginForm, EditProfileForm, PasswordChangingForm
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.views import PasswordChangeView
#from dashboard.home.models import Trading
#from .forms import EditTradingForm
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth import login, authenticate
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.template import loader
# Create your views here.

def creatingOTP():
    otp = ""
    for i in range(6):
        otp+= f'{random.randint(0,9)}'
    return otp

def sendEmail(email):
    otp = creatingOTP()
   # html_message = loader.render_to_string('accounts/email_template.html',{'otp': otp, 'subject':  'Thank you from'})
   # send_mail('One Time Password','Your OTP pin is',settings.EMAIL_HOST_USER,[email],fail_silently=True,html_message=html_message)
    return otp


def createUser(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CreateUser(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                otp = sendEmail(email)
                dt = PreRegistration(first_name=form.cleaned_data['first_name'],last_name=form.cleaned_data['last_name'],username= form.cleaned_data['username'],email=email,otp=otp,password1 = form.cleaned_data['password1'],password2 = form.cleaned_data['password2'])
                dt.save()
                return redirect("verify")
                
        else:
            form = CreateUser()
        return render(request,"register.html",{'form':form})
    else:
        return redirect('success')

def login_function(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request,data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                usr = authenticate(username=username,password = password)
                if usr is not None:
                    login(request,usr)
                    next = request.GET.get('next', reverse('home'))
                    return HttpResponseRedirect(next)
                    #return redirect('home')
        else:
            form = LoginForm()
        return render(request,'login.html',{'form':form})
    else:
        return redirect('home')

def verifyUser(request):
    if not request.user.is_authenticated:
        profile_id = request.session.get('ref_profile')
        print('profile_id', profile_id)
        if request.method == 'POST':
            form = VerifyForm(request.POST)
            if form.is_valid():
                otp = form.cleaned_data['otp']
                data = PreRegistration.objects.filter(otp = otp)
                if data:
                    username = ''
                    first_name = ''
                    last_name = ''
                    email = ''
                    password1 = ''
                    for i in data:
                        print(i.username)
                        username = i.username
                        first_name = i.first_name
                        last_name = i.last_name
                        email = i.email
                        password1 = i.password1
                    user = User.objects.create_user(username, email, password1)
                    user.first_name = first_name
                    user.last_name = last_name
                    user.save()
                    subject = 'Welcome to ALTON CAPITAL TRADE'
                    message = f'Hello {username}, \n Thank you for signing up on ALTON CAPITAL TRADE You are obviously a person with high taste.\n \n ALTON CAPITAL TRADE  will be your genuinee finance associate. Our aspiration is your prosperity! Board on this adventure that leads towards your success. Invest with ALTON CAPITAL TRADE and achieve your desires with reliance.\n \n \n We’re always on hand to help.\n Once again,\n welcome to the Krypto life!\n \n-ANDREW SMITH! \n Founder & CEO'
                    from_email = settings.EMAIL_HOST_USER
                    recipient_list = [email]
                    #html_message = loader.render_to_string('accounts/welcome_email.html',{'user_name': username, 'subject':  'Thank you from'})
                   # send_mail(subject,message,from_email,recipient_list,fail_silently=True,html_message=html_message)
                    usr_in = authenticate(username=username, password1=password1)
                    login(request,user)
                    return redirect('home')
                    data.delete()
                    #messages.success(request,'Account is created successfully! Please Login')
                  #  return redirect('login')   
                else:
                    messages.success(request,'Entered OTO is wrong')
                    return redirect('verify')
        else:            
            form = VerifyForm()
        return render(request,'verify.html',{'form':form})
    else:
        return redirect('success')

def success(request):
    if request.user.is_authenticated:
        return render(request,'html/success.html')
    else:
        return HttpResponseRedirect('/')

def logout_function(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

class UserEditView(generic.UpdateView):
    form_class =  EditProfileForm
    template_name = "accounts/edit_profile.html"
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user

def password_success(request):
    return render(request, 'accounts/password_success.html', {})


class PasswordsChangeView(PasswordChangeView):
    from_class = PasswordChangingForm
    #from_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')

