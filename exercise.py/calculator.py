a=float(input("Enter the number a = "))
b= float(input("Enter the number b = "))

operator= input("Enter the arthmatic operator = ")

match operator:

    case '+':
        print (f"The sum of the {a} and {b} is =  ",a+b)

    case '-':
        print("The difference between {a} and {b} is = ",a-b)
    
    case '*' :
        print("The product of {a} and {b} is = ",a*b)

    case '/':
        print("The divison of {a} and {b} is = ",a/b)

    case '%':
        print("The remainder of {a} and {b} is = ",a%b)