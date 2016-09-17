import sys, os
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "netflix.settings")

import django

django.setup()

from django.contrib.auth.models import User

def save_user_from_row(user_row):
    user = User()
    user.id = user_row['id']
    user.username = 'user-' + str(user_row['id'])
    user.save()

if __name__ == "__main__":

    #users = pd.read_table('data/ml-1m/users.dat',sep='::',names=['id','gender','age','occupation','zip'],engine='python')

    u_cols = ['id', 'age', 'sex', 'occupation', 'zip_code']
    users = pd.read_csv('data/ml-100k/u.user', sep='|', names=u_cols, encoding='latin-1')
    print len(users)

    users.apply(
        save_user_from_row,
        axis=1
    )

    print "There are {} users".format(User.objects.count())
