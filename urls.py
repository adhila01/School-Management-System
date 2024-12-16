from operator import index

from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('index/',index),
    path('reg/',register_student),
    path('login/',login_student),

    path('pro/',userprofile)
]
