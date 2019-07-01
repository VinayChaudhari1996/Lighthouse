"__Author__" = "Amar Singh"

t1 = (1,2,3,4,5) # create tuple
print(t1) # return all tuple data
print(type(t1)) # return type of data

print(t1[1]) # return 2nd index value

# Note:- tuple is immutable data types we cany modified directaly

# if you want  to modified tuple item You can change tuple to list 
# using list keyword 
list1 = list(t1)  # change tuple to list

# after modification u can also change
t1= tuple(list1)

