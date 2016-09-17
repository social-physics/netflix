from django.contrib import admin

from .models import Movie, Rating

class MovieAdmin(admin.ModelAdmin):
    model = Movie
    list_display = ('id', 'title')
    search_fields = ['id', 'title']

admin.site.register(Movie, MovieAdmin)

class RatingAdmin(admin.ModelAdmin):
    model = Rating
    list_display = ('movie_id', 'rating', 'user_id')
    list_filter = ['rating']

admin.site.register(Rating, RatingAdmin)