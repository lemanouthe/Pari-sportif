from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.http import Http404
import requests
from pariSportif.models import *
from django.views.generic import TemplateView
from django.conf import settings

# Create your views here.
def index(request):
    return render(request, 'index.html')

def equipes(request):
    post = Equipe.objects.all()
    return render(request, 'parisportif/equipes.html', {'post': post, 'media_url':settings.MEDIA_URL})

def pilotes(request):
    var_equipes = Equipe.objects.all()
    return render(request, 'parisportif/pilotes.html', {'var_equipes': var_equipes, 'media_url':settings.MEDIA_URL})
def myLogin(request):
    username = request.POST.get('username',False)
    password = request.POST.get('password',False)
    user = authenticate(username = username,password = password)
    if user is not None:
        login(request,user)
        return render(request, 'index.html')
    else:
        return render(request, 'pariSportif/login.html')

def register(request):
    username = request.POST.get('username',False)
    password = request.POST.get('password',False)
    email = request.POST.get('email',False)
    try:
        print(username,password,email)
        user = User(username = username)
        user.save()
        user.password = password
        user.set_password(user.password)
        user.save()
        user.email = email
        user.set_email(user.email)
        user.save()
    except:
        print('remplir le formulaire')
    return render(request, 'pariSportif/inscription.html')

@login_required(login_url = '/login')
def profile(request):
    return render(request, 'pariSportif/profile.html')

def mylogout(request):
    logout(request)
    return render(request, 'pariSportif/login.html')

def agenda(request):
    return render(request, 'pariSportif/calendrier.html')

def rang(request):
    return render(request, 'pariSportif/classements.html')
