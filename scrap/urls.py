from django.urls import path
from .views import *

urlpatterns = [
    
    path("scrap/", ScrapAPI.as_view()),
]

