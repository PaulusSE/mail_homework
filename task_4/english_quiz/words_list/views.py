from django.shortcuts import render
from database import words_database
from django.http.response import JsonResponse


def words_list(request, user):
    user_list = {}
    counter = 0
    for i in words_database:
        if words_database[i]['user'] == str(user):
            counter += 1
            user_list[counter] = (words_database[i])
    return JsonResponse(user_list)
