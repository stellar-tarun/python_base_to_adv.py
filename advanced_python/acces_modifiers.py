# 1.Public acess specifier

# class Employee:
#     def __init__(self):
#         self.name="Tarun"

# a=Employee
# print(a.name)


# 2.Private access specifier

# class student:
#     def __init__(self):
#         self.__name="Harry"

# a=student()
# # print(a.__name)  #cannot be accessed

# # can be acess 
# print(a._student__name)

# 3.Protected acess specifier

# class student:
#     def __init__(self):
#         self._name="Harry"

#     def _funName(self):
#         return "CodeWithHarry"
    
# class subject(student):
#     pass

# obj1=student()
# obj2=subject()

# # calling by object of student class
# print(obj1._name)
# print(obj1._funName())

# # calling by object of subject class
# print(obj2._name)
# print(obj2._funName())