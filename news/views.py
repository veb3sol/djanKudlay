from django.shortcuts import render
from django.http import HttpResponse

from .models import News

def index(request):
    print(dir(request)) # посмотреть все методы request
    return HttpResponse('Hello world')

# def index(request):
#     news = News.objects.order_by('-created_at')
#     return render(request, 'news/index.html', context = {'news': news, 'title': 'Список новостей'})


