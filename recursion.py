# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*factorial(n-1)
    
# f=factorial(5)
# print(f)
# fibonacci series

def fibonacci(n):
    if(n==0):
        return 0
    elif(n==1) :
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2) 
    
f = int(input("Enter the value of n = "))
fibonacci(f)
