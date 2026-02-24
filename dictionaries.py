# info={'name':'Karan','age':19,'eligible':True}
# print(info)


# #Accessing single values

# # Same
# print(info['name'])
# print(info.get('name'))  #print none if key doesn't exist
# print(info.get('name2'))



# #Accessing multiple values

# print(info.values())

# #or

# for key in info.keys():
#     print(info[key])



#Dictionaries Methods

ep1={122:45,123:89,567:69}
ep2={222:67,566:90}

ep1.update(ep2)
print(ep1)