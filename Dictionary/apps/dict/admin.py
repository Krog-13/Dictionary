from django.contrib import admin
from .models import Tenses, Phrase


@admin.register(Tenses)
class NameTense(admin.ModelAdmin):
    list_display = ('id', 'name', 'descriptions', 't_form', 'url')
    list_display_links = ('name',)

@admin.register(Phrase)
class NamePhrase(admin.ModelAdmin):
    list_display = ('id', 'engphrase', 'translate', 'tenses')
    list_display_links = ('tenses',)