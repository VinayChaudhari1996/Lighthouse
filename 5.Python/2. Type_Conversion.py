"""
The process of converting the value of one data type (integer, string, float, etc.) to another data type is called type conversion. Python has two types of type conversion.

Implicit Type Conversion
Explicit Type Conversion

"""


#  converting Integer to float

num_1 = 111
num_2 = 10.9

sum = num_1 + num+2

print("data type of num_1 :",type(num_1))  # int type
print("data type of num_2 :",type(num_2)) # float type

print("---------------------------------------------")

print("total of sum:",sum)  # 121.9

#  here the int + flaot will be changed float type

print("data type of sum :",type(sum))  # float type


#  adding the str and int data type 

num = 100
my_str = "Hello"

sum = num+my_str

print(sum)

#  Output : TypeError: unsupported operand type(s) for +: 'int' and 'str'


#  explicit Conversion

num_3 = 200
num_4 = '100'  # its str type

print("type of num_3",type(num_3))
print("type of num_4",type(num_4))

num_4 = int(num_4) # convert str num_4 to int num_4

print("type of num_4", type(num_4))


sum = num_3 +_ num_4

print("after converting num_4 str to int ", sum)
print("type of sum:", sum)













