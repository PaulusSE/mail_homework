from django.shortcuts import render
from django.http.response import HttpResponseBadRequest, HttpResponseRedirect
from database import words_database


def home(request):
    """Главная страница"""
    if request.method == 'GET':
        context = {'contents': words_database.values}
        return render(request, 'index.html', context=context)
    # else:
    #     return HttpResponseBadRequest()

    elif request.method == 'POST':
        user = request.POST.get('user')
        return HttpResponseRedirect(f'/words_list/{user}')


def add_word(request):
    """Форма создания нового поста"""
    if request.method == 'POST':
        word_id = len(words_database) + 1
        new_word = {
            'word_id': word_id,
            'en_word': request.POST.get('en_word'),
            'ru_word': request.POST.get('ru_word'),
            'user': request.POST.get('user'),
            'word_img': request.POST.get('')
        }
        # print(request.POST)
        words_database[word_id] = new_word
        return HttpResponseRedirect(f'/words/{word_id}')
    if request.method == 'GET' or request.method == 'PUT':
        return render(request, "add_word.html")
    return HttpResponseBadRequest()
