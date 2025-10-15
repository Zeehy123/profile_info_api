from django.urls import path

from .views import me, home

urlpatterns = [
   path('', home, name='home'),
    path('me/', me, name='me'),
]