from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate ,login
from registration_app import forms
from .forms import Registration_form
from django.contrib.auth.forms import  AuthenticationForm ,PasswordChangeForm,PasswordResetForm
from django.http import (
    HttpResponseNotAllowed, HttpResponseRedirect,
    HttpResponseForbidden, HttpResponseNotFound,
)
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import views as auth_views
from django.views.generic import ListView
from prod_cat_app.models import Category , Products
from cart.models import Cart
import datetime

# Create your views here.

def home_view(request):
    print('the session is ',request.session.get('cart_id','Unknown'))
    response = redirect('/home/')
    return response

# class HomePage(ListView): this view viewing categories in home page with easy way
#     model = Category
#     context_object_name = 'category_list'
#     template_name = 'home.html'
##### this view is for home page with setting the session####################################


def home_page(request):
    cart_id = request.session.get('cart_id', None)
    qs = Cart.objects.filter(id=cart_id)
    # qs2= Cart.objects.get(id=cart_id)
    # print(qs2.product)
    if qs.count() == 1 :
        if request.user.is_authenticated:
            Cart.objects.filter(id=cart_id).update(user=request.user)
        else:
            cart_obj = qs.first()
    else:
        if request.user.is_authenticated:
            cart_obj = Cart.objects.create(user=request.user)
            request.session['cart_id'] = cart_obj.id
        else:
            cart_obj = Cart.objects.create(user=None)
            request.session['cart_id'] = cart_obj.id
    categories = Category.objects.all()
    return render(request,'home.html', {'context':categories})
###############################################################
def signup_view(request):
    #print('the session key is ',request.session.session_key)
    register_form = forms.Registration_form()
    if request.method=='POST':
        register_form = Registration_form(request.POST)
        if register_form.is_valid():
            #print(register_form.is_valid())
            register_form.save()
            return HttpResponseRedirect('/loginpage/')
        else:
            return render(request,'registration/register_page.html',{'form':register_form})
    else:
        return render(request,'registration/register_page.html',{'form':register_form})

###########################################################################3
def login_view(request):
    form = AuthenticationForm()

    if request.method == 'POST':

        form = AuthenticationForm(request=request , data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email , password=password)
            print('the user is',user)
            if user is not None:
                login(request, user)
                if request.GET.get('next') != None:
                    return redirect('cart:checkout')
                else:
                    return redirect('/')
            else:
                return redirect('/')
        else:
            return render(request,'registration/loginpage.html',{'form':form})
    else:
        return render(request,'registration/loginpage.html',{'form':form})
#################################################################################
def change_pwd(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/changepwd/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/changepassword.html', {
        'form': form
    })

class PasswordResetView(auth_views.PasswordResetView):
     form_class = PasswordResetForm
