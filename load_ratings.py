import sys, os
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "netflix.settings")

import django

django.setup()

from movies.models import Rating

def save_rating_from_row(rating_row):
    rating = Rating()
    rating.movie_id= rating_row['movie_id']
    rating.user_id = str(rating_row['user_id'])
    rating.rating = str(rating_row['rating'])
    rating.save()


if __name__ == "__main__":

    #ratings = pd.read_table('data/ml-1m/ratings.dat',sep='::',names=['user','movie','rating','time'],engine='python')

    r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
    ratings = pd.read_csv('data/ml-100k/u.data', sep='\t', names=r_cols, encoding='latin-1')
    print len(ratings)

    ratings.apply(
        save_rating_from_row,
        axis=1
    )

    print "There are {} ratings".format(Rating.objects.count())
