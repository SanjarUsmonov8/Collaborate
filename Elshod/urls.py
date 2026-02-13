from django.urls import path
from Elshod.views import ElshodAPI

urlpatterns = [
    path('', ElshodAPI.as_view())
]