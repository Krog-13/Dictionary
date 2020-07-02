from django.shortcuts import render, redirect
from .models import Tenses, Phrase
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .forms import ReviewForm

class TensesViews(ListView):
    model = Tenses
    queryset = Tenses.objects.all()
    context_object_name = 'tenses'
    template_name = 'dict/index.html'

class TensesDitail(DetailView):
    model = Tenses
    slug_field = 'url'
    context_object_name = 'dict'
    template_name = 'dict/list_dict.html'

class PrhaseAdd(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        dicti = Tenses.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.tenses = dicti
            form.save()
        return redirect(dicti.get_absolute_url())
