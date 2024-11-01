from django.shortcuts import render
from django.views.generic import TemplateView


def index_task4_p(request):
    title = 'WOW servers'
    context = {
        'title': title,
    }
    return render(request, 'fourth_task/platform.html', context)
    # return render(request, 'fourth_task/games.html', context)

def index_task4_g(request):
    server_list = {
        'servers': ['Sirus', 'Uwow', 'WOW Circle'],
    }
    return render(request, 'fourth_task/games.html', context=server_list)

def index_task4_c(request):
    title = 'WOW cart'
    context = {
        'title': title,
    }
    return render(request, 'fourth_task/cart.html', context)