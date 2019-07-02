"__Author__"=="Amar Singh"

# conditional Statement

var = 5
# var = int(input("Enter Your Number:"))

if var==5:
    print("Found")

# now if-else

if var==5:
    print("Found") # if condition is true its return true(Found)

else:
    print("Not found") # if condition false its return (Not found )


# if-else-elif  for multiple condition handling You can use multiple elif
# in between if and else 

var = int(input("Enter your Number:"))

if var == 5:
    print("found",var)

elif var==10:
    print("found",var)

else:
    print("Not Found",var)


# Nested if create if inside if 

var = int(input("Enter Your Number:"))

if var >=0:
    if var==0:
        print("Zero")
    else:
        print("positive number")

else:
    print("Negative number")
