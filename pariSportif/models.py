from django.db import models
from django.contrib import auth

# Create your models here.

class Equipe(models.Model):
    name_equipes = models.CharField(max_length=100)
    titre = models.CharField(max_length=100)
    Pays = models.CharField(max_length=100)
    Drapeau = models.ImageField(upload_to= 'pictures')
    Icone = models.ImageField(upload_to='pictures')

    def __str__(self):
        return self.name_equipes

class Pilotes(models.Model):
    nom_pilote = models.TextField()
    numéro = models.IntegerField()
    date_naissance = models.DateField(auto_now=True)
    nationalité = models.CharField(max_length=100)
    image = models.ImageField(upload_to= 'pictures')
    drapeau_pilote = models.ImageField(upload_to= 'pictures')
    equipe = models.ForeignKey('Equipe', on_delete=models.CASCADE, null=True, related_name="equipes_pilote")

    def __str__(self):
        return self.nom_pilote

class Calendriers(models.Model):
    pays_icone = models.ImageField(upload_to='pictures')
    date_debut = models.DateField(auto_now=True)
    date_fin = models.DateField(auto_now=True)
    nom_course = models.CharField(max_length=80)
    ville_course = models.CharField(max_length=150)

    def __str__(self):
        return self.nom_course
