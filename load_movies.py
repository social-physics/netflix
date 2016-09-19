import sys, os
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "netflix.settings")

import django

django.setup()

from movies.models import Movie

def save_movie_from_row(movie_row):
    movie = Movie()
    movie.id = movie_row['movie_id']
    movie.title = movie_row['title']
    movie.rating = movie_row['rating_mean']
    movie.save()


if __name__ == "__main__":

    #movies = pd.read_table('data/ml-1m/movies.dat',sep='::',names=['id','title','genre'],engine='python')

    m_cols = ['movie_id', 'title', 'release_date', 'video_release_date', 'imdb_url']
    movies = pd.read_csv('data/ml-100k/u.item', sep='|', names=m_cols, usecols=range(5), encoding='latin-1')

    r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
    ratings = pd.read_csv('data/ml-100k/u.data', sep='\t', names=r_cols, encoding='latin-1')

    movie_info = movies[['movie_id', 'title']]
    movie_rating = ratings[['movie_id', 'rating']].groupby('movie_id')
    movie_rating_mean = movie_rating.mean().add_suffix('_mean').reset_index()

    movie_merge = pd.merge(movie_info, movie_rating_mean)

    movie_merge.apply(
        save_movie_from_row,
        axis=1
    )

    print "There are {} movies".format(Movie.objects.count())
