from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def index1(request):
    text = 'About LOVE'
    name = 'Viktor'
    number = 777
    list = ['3.785642', 'ttt', 'yyy']
    len_list = len(list)
    context = {
        'text': text,
        'name': name,
        'number': number,
        'list': list,
        'len_list': len_list
    }
    return render(request, 'index.html', context)

# class index2(TemplateView):
#     template_name = 'index2.html' причины того, почему закомментировали, расписаны в urls. Мы не стали делать
#     через дополнительный класс тут, а импортировали TemplateView прямо в urls.
