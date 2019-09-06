user = int(input("Enter your value:"))
from time import process_time


def factorial(n):
  fact = 1
  for i in range(1,n+1):
    fact = fact * i
  return fact


start = process_time()
print("Factorial of {} no is {}".format(user,factorial(user)))
end = process_time()
print("Required time to complete process:", end-start)