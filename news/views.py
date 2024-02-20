from django.shortcuts import render
from django.http import HttpResponse

from .models import News, Category

# def index(request):
    # print(dir(request)) # посмотреть все методы request
    # return HttpResponse('Hello world')

def index(request):
    news = News.objects.order_by('-created_at')
    categories = Category.objects.all()
    context = {
        'news': news,
        'categories': categories,
        'title': 'Список новостей'
    }
    return render(request, 'news/index.html', context = context)


def get_category(request, category_id):
    news = News.objects.order_by('-created_at').filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'categories': categories,
        'category': category,
    }
    return render(request, 'news/category.html', context = context)
