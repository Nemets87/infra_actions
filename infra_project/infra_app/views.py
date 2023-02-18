from django.http import HttpResponse


def index():
    return HttpResponse('У меня получилось!')


def second_page():
    return HttpResponse('А это вторая страница!')
