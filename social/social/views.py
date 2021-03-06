from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from . import forms
from author.models import Author
import sys

#Create your views

# The home page for registration and login.
def index(request):
    try:
        if request.user.is_authenticated() and Author.objects.get(id=request.user):
            return HttpResponseRedirect('/author/')
    except:
        return render(request, 'login/index.html')
    return render(request, 'login/index.html')

# Register a user
def register(request):
    # Only process the registration if it is a POST request
    if (request.method != 'POST'):
        return HttpResponseRedirect('/')
    
    regForm = forms.RegistrationForm(request.POST)
    
    # Check if the form is valid
    if (not regForm.is_valid()):
        return render(request, 'login/index.html',{'errors':'Username (case-sensitive) already in use. Please try again.'})

    # Create and save the User and Author model.
    # Both need to be saved because there is no point of saving one with out the other since
    # they are in a one-to-one relationship.
    userEmail = request.POST['email']
    try:
        if User.objects.get(email=userEmail):
            return render(request, 'login/index.html',{'errors':'E-mail already in use. Please use another.'})
    except:
        user = regForm.save() # Save the form data
        # Ref: http://stackoverflow.com/questions/2936276/django-modelforms-user-and-userprofile-not-hashing-password
        user.set_password(user.password) # Set the password
        user.is_active = True
        user.save() # Push to db
        newUser = User.objects.get(email=userEmail)
        # Create and save the Author model
        author = Author(id=newUser)
        author.setDisplayName()
        author.setAuthorURL()
        author.setApiID()
        author.save()
        return render(request, 'login/index.html',{'success':'Signed up! Please wait for admin approval.'})
    
    return render(request, 'login/index.html',{'errors':'An error occurred. Please try again.'})

# User login
def login(request):
    # Only process the login if it is a POST request
    if (request.method != 'POST'):
        return HttpResponseRedirect('/')

    email = request.POST['user']
    password = request.POST['password']

    # Get the user. Doubles as making sure the user exists.
    try:
        logInUser = User.objects.get(email=email)
        author = Author.objects.get(id=logInUser)
    except:
        return render(request, 'login/index.html',{'errors':'Invalid e-mail or password. Please try again.'})
        
    if not author.approved:
        return render(request, 'login/index.html',{'errors':'User has not been approved by system admin yet. Please try again later.'})

    author = authenticate(username=logInUser.username, password=password)
    if author is not None:
        django_login(request, author)
        return redirect('/author/')
    
    return render(request, 'login/index.html',{'errors':'Invalid e-mail or password. Please try again.'})

@login_required()
def logout(request):
    django_logout(request)
    return HttpResponseRedirect('/')
