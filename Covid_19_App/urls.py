from django.urls import path
from Covid_19_App.views import *

urlpatterns = [
    path('', index, name='index'),
]
