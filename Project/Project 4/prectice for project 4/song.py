class Song:
    def __init__(self,name):
        self.__name = name
    def set_name(self,name):
        self.__name = name
    def get_name(self):
        return self.__name
    def __str__(self):
        return 'The name of song is:' + str(self.__name)