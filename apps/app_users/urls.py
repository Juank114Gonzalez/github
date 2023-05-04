from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name = "login"),
    path('registration/', UserRegistration.as_view(), name = "register_user"),
]