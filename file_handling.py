# 1

# f=open('myfile.txt','r')
# # print(f)
# text=f.read() 
# print(text)
# f.close()

# 2

# # it will replace the old text
# f=open('myfile.txt','w')
# # text=f.write("badhiya bhai tu suna")
# # print(text)

# f.write('bhadiya bhai tu suna')

# f.close()

# 3

# #it will add the text after the old written text

# f=open('myfile.txt','a')

# f.write('\nbadhiya bhai tu suna....!')
# f.close()


# 4
# no need to end the code with f.close syntax by (with) it not need to end the code with close keyword
# with open('myfile.txt','a'):
    # f.write("Hey i am inside with")

# 5
# # to read single line from the file....if we want to read multiple lines,we can use a loop....!!
# f=open('myfile.txt','r')
# while True:
#     line=f.readline()
#     if not line:
#         break
#     print(line)


#6
# # # to write line
# f=open('myfile.txt','w')
# lines=['hey \n', 'hru \n','good...what about you....?']
# f.writelines(lines)


# 7
# with open('myfile.txt','r') as f:
# # 10th byte ke baad
#  f.seek(10)

# # read the 5 byte after the 10th byte
#  data=f.read(5)
#  print(data)



