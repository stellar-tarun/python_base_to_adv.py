import os
# to create the directory 
os.mkdir("Data")


#to create many folder

for i in range (0,100):
    os.mkdir(f"Data/Day{i+1}")

#open the file in read-only mode
f=os.open("My_file.txt",os.O_RDONLY)

# #read the contents of the file
# contents=os.read(f,1024)


# #close the file
# os.close(f)

