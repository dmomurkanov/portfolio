from . import views
from django.urls import path

from .views import main_banner

urlpatterns = [
    path("", main_banner),
]

