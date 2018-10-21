import Movie
from .song import Song
import csv


#  Write program that allows a user to perform binary search on a collection of Movie/Song objects
#  Ask user to enter name of movie/song
#  Write program that makes a list of 100 random numbers between 1-100.
#  Sort it using selection or insertion sort, then print list.



movie_name = input('Enter the name of movie:')
print(Movie(movie_name))

song_name = input('Enter the name of song:')
print(Song(song_name))
