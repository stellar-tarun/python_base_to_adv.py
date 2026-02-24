# class Person:
#     name="Tarun"                                                       
#     occ="Student"
    
#     def info(self):
#         print(f"{self.name} is a {self.occ}")

# a=Person()
# a.name="Harry"
# a.occ="Developer"
# a.info()



class Person:

    def __init__(self,name,occ):
        self.name=name 
        self.occ=occ

    def info(self):
        print(f"{self.name} is a {self.occ}.")

a=Person("Tarun","Student")
a.info()