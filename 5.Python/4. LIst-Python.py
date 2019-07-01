_"__Author__" = "AMAR SINGH"

# LIST in Python

l1 = [1,2,3,4,5,6]  # Create a list
l2 = [8,9,10]

print(l1) # printing all data of list

print(l1[0]) # return first value
l1[1]= 5 # change the index 1 value

l1.append(7) # appending the last of the list
l1.extend(l2) # adding the all data of list 2 in list 1
print(l1)

l1.pop(0)   #remnove 0th index value
l1.pop()  # remove last value of list
l1.remove(2) # remove value (2)--> value not index
print(l1)

len(l1) # find the length of the list

l1.insert(0,1) # insert the value specified index (0--> index,1==>value)
print(l1)

print(l1.count(3)) # counting value how many times present 

l1.reverse()  # reverse the all data in list

print(l1)

# note :- there is more builtin function You can read and  practice using documentation
