# class Employee:
#     company="Apple"

#     def show(self):
#         print(f"The name is {self.name} and the company name is {self.company}.")

#         def changeCompany(cls,newCompany):
#             cls.company=newCompany

# e1=Employee()
# e1.name="Tarun"
# e1.show()

# e1.changeCompany("Tesla")
# e1.show()
# print(Employee.company)



# class Employee:
#     company="Apple"

#     def show(self):
#         print(f"The name is {self.name} and the company name is {self.company}.")
#     @classmethod  #ab company ka name such me change hoga

                                                                                         
#     def changeCompany(cls,newCompany):
#             cls.company=newCompany

# e1=Employee()
# e1.name="Tarun"
# e1.show()

# e1.changeCompany("Tesla")
# e1.show()
# print(Employee.company)




# Class method as Alternate Constructor

# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary

# e1=Employee("Harry",12000)
# print(e1.name)
# print(e1.salary)


# string="Jhon-12000"
# e2=Employee(string.split("-")[0],string.split("-")[1])
# print(e2.name)
# print(e2.salary)  

#Toh iss code ko simplify karne ke liye 


class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    @classmethod
    def fromStr(cls,string):
        return cls(string.split("-")[0],string.split("-")[1])
    # yha par ye simpify ho gaya hai sath me ab ise e2,e3,e4 ke liye bhi use kar sakte hai
e1=Employee("Harry",12000)
print(e1.name)
print(e1.salary)


string="Jhon-12000"
e2=Employee.fromStr(string)
print(e2.name)
print(e2.salary)  

