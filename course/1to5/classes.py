class Humman:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f'i am {self.name}')


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print('move')

    def draw(self):
        print('draw')

class Person(Humman):
    pass



mau = Person("maurizio")

mau.talk()

bob = Person("boob")
bob.talk()