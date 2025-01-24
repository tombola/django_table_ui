from django.contrib import admin
from django.urls import path

from seeds.views import varieties_view

urlpatterns = [
    path("varieties/", varieties_view),
]
