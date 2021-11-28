from django.shortcuts import render
from database import words_database
from django.http.response import JsonResponse


def show_word(request, word_id):
    return JsonResponse(words_database[word_id])


# def words_list(request, user):
#     # user_list = []
#     # for i in words_database:
#     #     if words_database[i]['user'] == str(user):
#     #         user_list.append(words_database[i])
#     return JsonResponse('*user_list')
