from django.urls import path
from users.views import login, registers

urlpatterns = [
    path('login', login, name='login'),
    path('registers', registers, name='registers'),
]

