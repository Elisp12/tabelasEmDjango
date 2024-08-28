from django.urls import path

from cultura.views import *

urlpatterns = [
    path('', home, name='home'),
    path('update/',update, name='upsdate'),
]