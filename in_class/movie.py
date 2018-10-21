class Movie:
    def __init__(self, title, releaseDate, rating, director):
        self.title = title
        self.releaseDate = releaseDate
        self.rating = rating
        self.director = director
        self.content = ''

# accessor (get methods)
    def getTitle(self):
        return self.title

    def getRealseDate(self):
        return(self.releaseDate)

    def getRating(self):
        return(self.rating)

    def getDirector(self):
        return(self.director)

# mutator(set methods)
    def setContent(self, content):
        self.content = content
    def setTitle(self, title):
        self.title = title
    def setRealseDate(self,releaseDate):
        self.releaseDate = releaseDate
    def setRating(self,rating):
        self.rating = rating
    def setsetDirector(self,director):
        self.director = director

# Str methods
    def __str__(self):
        result = self.title + '\n' + self.releaseDate +'\n' + self.rating + '\n' + self.director + '\n' + self.content
        return result