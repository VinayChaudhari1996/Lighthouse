import multiprocessing
import threading
from time import process_time


list_fact = []
def factorial(number):
    a = 1
    for i in range(1,number+1):
        a *=i
    list_fact.append(a)


def count_processor():
    return multiprocessing.cpu_count()
processor = count_processor()

user_input = int(input("Enter user input:"))
thread_input = user_input//processor
print(thread_input)

start = process_time()

for i in range(processor):
    
    t1 = threading.Thread(target=factorial,args=(thread_input,))
    t1.start()
    t1.join()
   
print(sum(list_fact))

end = process_time()
print( "time count",end - start)





    