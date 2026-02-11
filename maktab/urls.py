from django.urls import path
from maktab.views import MaktabAPI

urlpatterns = [
    path('',MaktabAPI.as_view())
]