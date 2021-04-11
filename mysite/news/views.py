from django.http import HttpResponse
from django.shortcuts import render

from .models import News, Category


def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
    }
    return render(request, 'news/index.html', context)


def test(request):
    return HttpResponse('<h1> Sup bro </h1>')


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id,)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news, 'category': category})
