from django.shortcuts import render
from django.views.generic import TemplateView


def index_task4(request):
    title = 'WOW servers'
    server_list = ['Sirus', 'WOW Circle']

    context = {
        'title': title,
        'server_list': server_list,
    }
    return render(request, 'fourth_task/platform.html', context)
