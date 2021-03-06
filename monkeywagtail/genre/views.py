from django.shortcuts import render, get_object_or_404
from .models import GenreClass


def genre_list(request):
    genres = GenreClass.objects.all()
    return render(request, 'genre/genre_list.html', {
        'genres': genres,
    })


def genre_detail(request, slug):
    genre = get_object_or_404(GenreClass, slug=slug)
    return render(request, 'genre/genre_detail.html', {
        'genre': genre,
    })
