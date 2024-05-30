from typing import Any
from django.http import HttpResponse
from django.shortcuts import render
from django.template import context
from django.template.defaultfilters import first


def index(request) -> HttpResponse:
    context: dict[str, Any] = {
        'title': 'Home',
        'content': 'Главная страница магазина - HOME',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'is_authenticated': False
    }
    return render(request, 'main/index.html', context)


def about(request):
    return HttpResponse('About page')

# Create your views here.
