class Bird:
    def __init__(self, name, birthday, breed, color):
        self.name = name
        self.birthday = birthday
        self.breed = breed
        self.color = color

    def get_name(self):
        return self.name

    def get_birthday(self):
        return self.birthday

    def get_breed(self):
        return self.breed

    def get_color(self):
        return self.color

    def set_name(self, name):
        self.name = name

    def set_birthday(self, birthday):
        self.birthday = birthday

    def set_breed(self, breed):
        self.breed = breed

    def set_color(self, color):
        self.color = color

    def __str__(self):
        return 'Pets names: ' + str(self.name) + '\n' + 'Birthday: ' + str(self.birthday) + '\n' \
               + 'Breed: ' + str(self.breed) + '\n' + 'Color: ' + str(self.color)
