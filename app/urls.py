from django.urls import path
from .views import *

urlpatterns = [
    path('', Menu),
    path('news/', Our_school),
    path('news/<int:pk>/', Detail),
    path('classes/<int:rubric_id>/', Klas)
]
