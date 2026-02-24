# class Person:
#     name="Tarun"
#     age=20
#     doing="Advanced Python"
#     belong="Meerut"

#     def info(self):
#         print(f"{self.name} belong to {self.belong}.")


# a=Person()
# a.info()







class Person:
    name="Tarun"
    age=20
    doing="Advanced Python"
    belong="Meerut"

    def info(self):
        print(f"{self.name} belong to {self.belong}.")


a=Person()
b=Person()
b.name="Harry"
b.belong="Uttar Pradesh"
a.info()
b.info()