question=["What's the capital of INDIA ? \nA.Delhi  B.Mumbai\nC.Goa    D.Noida"]
print(question)
Your_Answer=input("Chose the correct option : ")

if (Your_Answer == "A"):
    print("You have won 10$.")

else:
    print("Wrong Answer")



question=["What's the capital of INDIA ?","Delhi","Mumbai","Goa","Noida",0]

levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]

for i in range (0,len(question)):
    question=question[i]

    print(f"Question for Rs. {levels[i]}")
    print(f"A.{question[1]}              B.{question[2]}")
    print(f"C.{question[3]}             D.{question[4]}")

    reply =int(input("Enter  your answer (1-4) "))
    if (reply == question[-1]):
        print("Correct answer,you have won Rs. {levels[i]}")
    
    else:
        print("Wrong Answer!")
        break