#Code-1
# class ParentClass:
#     def parent_method(self):
#         print("This is the parent method.")

# class ChildClass(ParentClass):
#     def parent_method(self):
#         print("Harry")
#         super().parent_method()
#     def child_method(self):
#         print("This is the child method.")
#         super().parent_method()

# child_object=ChildClass() #object create kiya hai child class ka
# child_object.child_method() #call ho rha hai function child class ka fir hoga kya ki uske niche jo super keyword use ho rha hai wo parent class ko call kardega fir wo print ho jayega
# child_object.parent_method() #yha child class ka parent method wala function call ho rha hai aur iske niche super keyword firse wahi kam kargega




#Code-2
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        super().speak()  # Calls Animal's speak
        print("Dog barks")

dog = Dog()
dog.speak()


#Code-3

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")
        super().show()

class C(A):
    def show(self):
        print("C")
        super().show()

class D(B, C):
    def show(self):
        print("D")
        super().show()

d = D()
d.show()
 