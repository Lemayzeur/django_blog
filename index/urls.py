from django.urls import path
from .views import premyePaj

urlpatterns = [
    path('premye', premyePaj)
]
