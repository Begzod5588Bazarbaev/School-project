from django.urls import path
from .views import *

urlpatterns = [
    path('', Menu),
    path('class/', Class) 
]
