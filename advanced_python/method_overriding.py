class Shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def area(self):
        return self.x * self.y

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
        super().__init__(radius,radius)

    def area(self):
        return 3.14 * super().area()


# rec=Shape(3,5)
# print(rec.area())  

c= Circle(5)
print(c.area())




# # Python program to demonstrate 
# # Defining parent class 
# class Parent(): 
	
# 	# Constructor 
# 	def __init__(self): 
# 		self.value = "Inside Parent"
		
# 	# Parent's show method 
# 	def show(self): 
# 		print(self.value) 
		
# # Defining child class 
# class Child(Parent): 
	
# 	# Constructor 
# 	def __init__(self): 
# 		super().__init__()  # Call parent constructor
# 		self.value = "Inside Child"
		
# 	# Child's show method 
# 	def show(self): 
# 		print(self.value) 
		
# # Driver's code 
# obj1 = Parent() 
# obj2 = Child() 

# obj1.show()  # Should print "Inside Parent"
# obj2.show()  # Should print "Inside Child"