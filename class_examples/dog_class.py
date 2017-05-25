class Dog(object):
    species = 'canine'

    def __init__(self, name, color, age):
        self.name = name.title()
        self.color = color.lower()
        try:
            self.age = int(age)
        except ValueError:
            print("{0} must have just been born since {0} can't be {1}".format(
                self.name, age))
            self.age = 0

    def about_me(self):
        print('I am a {} named {} who is {} and {} years old'.format(
            self.species, self.name, self.color, self.age))

    def grow_older(self, years=1):
        self.age += years


class Cat(Dog):
    species = 'feline'
