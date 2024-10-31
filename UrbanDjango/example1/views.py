from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def index(request):
    return render(request, 'index.html')

# class index2(TemplateView):
#     template_name = 'index2.html' причины того, почему закомментировали, расписаны в urls. Мы не стали делать
#     через дополнительный класс тут, а импортировали TemplateView прямо в urls.
