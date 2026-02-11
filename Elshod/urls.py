from django.urls import path
from Elshod.views import salom

urlpatterns = [
    path('', salom)
]