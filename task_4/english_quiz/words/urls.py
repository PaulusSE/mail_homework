from django.urls import path
from .views import show_word

urlpatterns = [
    path('<int:word_id>/', show_word, name='show_word'),
]
