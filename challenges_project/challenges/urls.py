"""
URL configuration for challenges app.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:month>', views.monthly_challenge_by_number, name='month-number'),
    path('<str:month>', views.monthly_challenge, name='month-challenge'),
    # path converters: str | int | slug | uuid | path
]
