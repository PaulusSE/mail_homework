from django.urls import path, include
from .views import home, add_word

urlpatterns = [
    path('', home, name='home'),
    path('add_word/', add_word, name='add_word'),
]
