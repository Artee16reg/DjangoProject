from django import template
from django.db.models import Count

from news.models import Category

register = template.Library()


# Можно удалить
@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('news/list_categories.html')
def show_categories():
    """вывод групп в _sidebar"""
    sum_news_all = Category.objects.annotate(Count('news'))
    count = 0
    for i in sum_news_all:
        count += i.news__count
    categories = Category.objects.annotate(cnt=Count('news')).filter(cnt__gt=0)
    return {"categories": categories, 'arg1': count}
