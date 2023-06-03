from django.urls import path
from .views import SignUp

urlpatterns = [
    path('login', SignUp.as_view(), name='login'),
]