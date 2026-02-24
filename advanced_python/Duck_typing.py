class Duck:
    def quack(self):
        print('Quack Quack')

class human:
    def quack(self):
        print('Yes Human')

duck = Duck()
person = human()
duck.quack()
person.quack()




class Bird:
    def fly(self):
        print("fly with wings")

class Airplane:
    def fly(self):
        print("fly with fuel")

class Fish:
    def swim(self):
        print("fish swim in sea")

for obj in Bird(),Airplane(),Fish():
    obj.fly()




class Dog:
    def speak(self):
        return "woof!"

class Cat:
    def speak(self):
        return "Meow!"

def animal_sound(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()
animal_sound(dog)
animal_sound(cat)