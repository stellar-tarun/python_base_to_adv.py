# 1.Single Inheritance

#Code -1

# class Employee:

#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
    
#     def showDetails(self):
#         print(f"The name of the Employee: {self.id} is {self.name}")

# class Programmer(Employee):
#     def showLanguage(self):
#         print("The default language is Python")

# e1=Employee("Rohan das",400)
# e1.showDetails()

# e2=Programmer("Harry",4100)
# e2.showDetails()

# e2.showLanguage()


#Code-2


# class Animal:
#     def __init__(self,name,species):
#         self.name=name
#         self.species=species

#     def make_sound(self):
#         print("Sound made by the animal.")

# class Dog(Animal):
#     def __init__(self,name,breed):
#         Animal.__init__(self,name,species="Dog")
#         self.breed =breed

#     def make_sound(self):
#         print("Bark !")

# d=Dog("Sam","labrador")
# d.make_sound()

# a=Animal("sam","Dog")
# a.make_sound()




# 2.Multiple Inheritance


class CanFly:
    def fly(self):
        print("Can fly")

class CanSwim:
    def swim(self):
        print("Can swim")

class Duck(CanFly, CanSwim):
    pass

d = Duck()
d.fly()   # Can fly
d.swim()  # Can swim


#3.Multilevel Inheritance

class Animal:
    def eat(self):
        print("Animal eats")

class Dog(Animal):  # B inherits from A
    def bark(self):
        print("Dog barks")

class Puppy(Dog):  # C inherits from B
    def weep(self):
        print("Puppy weeps")

p = Puppy()
p.eat()   # Inherited from Animal
p.bark()  # Inherited from Dog
p.weep()  # Defined in Puppy


#4.Hierarchical Inheritance

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

d = Dog()
d.sound()  # Inherited
d.bark()

c = Cat()
c.sound()  # Inherited
c.meow()


#5.Hybrid Inheritance

class Animal:
    def eat(self):
        print("Animal eats")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

class Pet(Dog, Cat):  # Multiple inheritance
    def play(self):
        print("Pet plays")

p = Pet()
p.eat()   # From Animal
p.bark()  # From Dog
p.meow()  # From Cat
p.play()  # Defined in Pet
