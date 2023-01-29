from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render

from movies.models import Movie

# data= {'movies': ['movie1', 'movie2']}
"""data = \
    {
        'movies':
            [
                {
                    'id': 3,
                    'title': 'Jaw',
                    'year': 1660
                },
                {
                    'id': 4,
                    'title': 'Sharkando',
                    'year': 1660
                },
                {
                    'id': 5,
                    'title': 'The Meg',
                    'year': 2000
                }
            ]
    }

"""


def homepage(request):
    return HttpResponse("Welcome to Home Page :-")


def movies(request):
    data = Movie.objects.all()
    return render(request, 'movies/movies.html', {'movies': data})


# return render(request, 'movies/movies.html', {'movies': ['movie1', 'movie2']})

def detail(request, id):
    data = Movie.objects.get(pk=id)
    return render(request, 'movies/detail.html', {'movie': data})


def add(request):
    title = request.POST.get('title')
    year = request.POST.get('year')
    if title and year:
        movie = Movie(title=title, year=year)
        movie.save()
        return HttpResponseRedirect('/movies')
    return render(request, 'movies/add.html')


def delete(request, id):
    try:
        movie = Movie.objects.get(pk=id)
    except:
        raise Http404("Movie doesn't exist ")
    movie.delete()
    return HttpResponseRedirect('/movies')
