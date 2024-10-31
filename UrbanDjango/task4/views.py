from django.shortcuts import render
from django.views.generic import TemplateView


def index_task4(request):
    title = 'WOW servers'
    context = {
        'title': title,
    }
    return render(request, 'fourth_task/platform.html', context)
