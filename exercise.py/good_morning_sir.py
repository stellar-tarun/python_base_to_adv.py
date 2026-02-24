import time

current_time =int( time.strftime("%H", time.localtime()))
# print(f"Current time: {current_time}")
if  12<current_time and current_time <22:
    print("Good Evening sir!")

elif 4< current_time and current_time <12:
    print("Good Morning sir!")

else:
    print("Good Night sir!")

