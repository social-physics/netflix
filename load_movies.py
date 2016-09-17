import sys, os
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "netflix.settings")

import django

django.setup()

from movies.models import Movie

def save_movie_from_row(movie_row):
    movie = Movie()
    movie.id = movie_row['id']
    movie.title = movie_row['title']
    movie.save()


if __name__ == "__main__":

    #movies = pd.read_table('data/ml-1m/movies.dat',sep='::',names=['id','title','genre'],engine='python')

    m_cols = ['id', 'title', 'release_date', 'video_release_date', 'imdb_url']
    movies = pd.read_csv('data/ml-100k/u.item', sep='|', names=m_cols, usecols=range(5), encoding='latin-1')
    print len(movies)

    movies.apply(
        save_movie_from_row,
        axis=1
    )

    print "There are {} movies".format(Movie.objects.count())
