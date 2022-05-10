from django.urls import path
from .views import home, student

urlpatterns = [
    path('', home, name='home'),
    path('students/', student, name='student'),
]
