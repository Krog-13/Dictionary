from django.urls import path
from . import views

urlpatterns = [
    path('', views.TensesViews.as_view(), name='Tenses_list'),
    path("<slug:slug>/", views.TensesDitail.as_view(), name='tense_detail'),
    path("review/<int:pk>/", views.PrhaseAdd.as_view(), name='add_phrase'),
]