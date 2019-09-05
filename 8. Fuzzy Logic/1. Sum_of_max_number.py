
# 1) some of maximum number provide by user input
##############################################
# Given :- [1,2,3,4,5]
# eg. where k=2 (sum should be highest 2 no) 
# o/p : 9



from random import shuffle
l = []

for i in range(1,11):
    l.append(i)

k = int(input("Enter size less than 10:"))
def check_hight(x):
    b = max(x)
    x.remove(b)
    return x,b
c = 0
for i in range(k):
    l,height =check_hight(l)
    c+=height
print(c)
