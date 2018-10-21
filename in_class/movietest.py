import movie

# main test program
def main():
    movie1 = movie.Movie('Zootopia','Mar.4, 2016','Rotten Tomatoes: 8.1/10','Byron Howard and Rich Moore')
    movie2 = movie.Movie('Fantastic Beasts','Nov 18, 2016','Rotten Tomatoes: 6.8/10','David Yates')
    movie3 = movie.Movie('Now you see me','May 31, 2013','Rotten Tomatoes: 5.7/10','Louis Leterrier')

    print('Movie 1:', movie1)
    print('Movie 2:', movie2)
    print('Movie 3:', movie3)

main()