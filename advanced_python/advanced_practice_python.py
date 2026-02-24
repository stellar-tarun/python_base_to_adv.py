# class Person:
#     name="Tarun"
#     age=20
#     occ="Student"

# obj=Person
# print(obj.name)
# print(obj.age)
# print(obj.occ)
# print("---------------------------")
# print(obj.name,obj.age,obj.occ)



# class Person:
#     name="Tarun"
#     age=20
#     occ="Student"

#     def info(self):
#         print(f"{self.name} is a {self.age} year old.")


# obj=Person()
# obj.info()
# print("---------------------")
# obj.name="Arun"
# obj.age=28
# obj.info()


# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def info(self):
#         print(f"{self.name} is {self.age} year old.")

# obj=Person("Tarun",20)
# obj.info()

# print("_____________________________")

# obj=Person("Arun",28)
# obj.info()



# Decorater

# def wish(fx):
#     def mfx():
#         print("Good Morning !")
#         fx()
#         print("Good Bye!")

#     return mfx

# @wish
# def hello():
#     print("Hello !")

# hello()





class student:
    def __init__(self,marks):
        self.marks=marks
    def showdetails(self):
        print(f"the marks of the students are {self.marks}.")

obj=student(80)
student.showdetails(obj)