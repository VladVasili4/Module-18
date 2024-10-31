from django.shortcuts import render
from django.views.generic import TemplateView


def index_task3(request):
    title = 'WOW servers'
    context = {
        'title': title,
    }
    return render(request, 'third_task/platform.html', context)
