from django import forms
from .models import Phrase, Tenses

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Phrase
        fields = ('engphrase', 'translate')