from django.urls import path
from .views import words_list

urlpatterns = [
    path('<str:user>/', words_list, name='words_list'),
    # path('', words_list, name='words_list'),

]
