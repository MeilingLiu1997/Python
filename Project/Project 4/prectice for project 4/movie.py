import random
class Movie:
    def __init__(self,name):
        self.__name = name

    def get_name(self):
        return self.__name

    def getNum(self):
        return random.randint(1, 100)

    def __str__(self):
        return 'The name of movie is:' + str(self.__name)