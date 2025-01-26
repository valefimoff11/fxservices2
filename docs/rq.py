import math

def make_sound(animal):
    return animal.sound()

class Dog:
    def sound(self):
        return "Bark"

class Cat:
    def sound(self):
        return "Meow"

animals = [Dog(), Cat()]
for animal in animals:
    #print(make_sound(animal))
    print(animal.sound())
    animal.name = "cat"
    print(animal.name)

    animal.ms = make_sound
    print(animal.ms(animal))

    print(animal is Dog)

u = 1mmmm
print(type(u) is int)
print(type(u))

print(2**3)
print(math.sqrt(9))