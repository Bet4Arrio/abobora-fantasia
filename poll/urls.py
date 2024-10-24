# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.fantasy_poll, name='fantasy_poll'),
    path('thank-you/', views.thank_you, name='thank_you'),  # Example thank you page
    path('fantasy/add/', views.add_fantasy, name='add_fantasy'),
    path('fantasy/vote-chart/', views.fantasy_vote_chart, name='fantasy_vote_chart'),

]
