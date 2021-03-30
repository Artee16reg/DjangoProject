from django.http import HttpResponse


def index(request):
    return HttpResponse('Здарова нахуй')


def test(request):
    return HttpResponse('<h1> Sup bro </h1>')
