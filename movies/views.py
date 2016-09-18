from django.shortcuts import get_object_or_404, render

from .models import Movie, Rating


def movie_list(request):
    movie_list = Movie.objects.order_by('-name')
    context = {'movie_list':movie_list}
    return render(request, 'movie_list.html', context)
