from django.conf.urls import url
from pariSportif import views
from django.contrib import admin
from django.views.generic import TemplateView



app_name = 'pariSportif'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^equipe/', views.equipes, name='equipes'),
    url(r'^pilote/', views.pilotes, name='pilotes'),
    url(r'^login/', views.myLogin, name='login'),
    url(r'^register/', views.register, name='register'),
    url(r'^profile/', views.profile, name = 'profile'),
    url(r'^logout/', views.mylogout, name='logout'),
    url(r'^agenda/', views.agenda, name='agenda'),
    url(r'^rang/', views.rang, name='rang'),
]
