from django.db import models
from django.urls import reverse


class Tenses(models.Model):
    name = models.CharField('Tense', max_length=30)
    descriptions = models.TextField(max_length=150)
    t_form = models.BooleanField(null=True, default=False)
    url = models.SlugField(max_length=1602, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("tense_detail", kwargs={'slug': self.url})

    class Meta:
        verbose_name = 'Tense'
        verbose_name_plural = 'Tenses'


class Phrase(models.Model):
    engphrase = models.CharField(max_length=30)
    translate = models.CharField(max_length=40, help_text='Enter your phrase is translate')
    gold_phrase = models.BooleanField('Золотой слиток',null=True, default=False)
    tenses = models.ForeignKey(Tenses, verbose_name='Tenses', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Phrase'
        verbose_name_plural = 'Phrases'