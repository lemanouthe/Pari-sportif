from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Equipe)

class EquipeAdmin(admin.ModelAdmin):
    list_display = ('name_equipes', 'titre', 'Pays', 'Drapeau', 'Icone',)
    list_filter = ("name_equipes",)
    search_fields = ('titre', 'Pays',)

    ordering = ['-name_equipes']

@admin.register(Pilotes)
class PilotesAdmin(admin.ModelAdmin):
    list_display = ('nom_pilote', 'numéro', 'date_naissance', 'nationalité', 'image', 'drapeau_pilote',)
    list_filter = ("nom_pilote",)
    search_fields = ('numéro', 'nationalité',)

    ordering = ['-numéro']

@admin.register(Calendriers)
class CalendriersAdmin(admin.ModelAdmin):
    list_display = ('pays_icone', 'date_debut', 'date_fin', 'nom_course', 'ville_course',)
    list_filter = ("date_debut",)
    search_fields = ('date_debut', 'date_fin',)

    ordering = ['-date_debut']

admin.site.site_header = "ADMIN"
admin.site.site_title = "ADMIN"
admin.site.index_title = "BIENVENU ADMIN"
