from django.urls import path

from cultura.views import home

urlpatterns = [
    path('', home, name='home'),
]