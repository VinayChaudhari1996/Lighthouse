import multiprocessing
import threading
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

t1 = threading.Thread(target=factorial,args=(thread_input,))
t2 = threading.Thread(target=factorial,args=(thread_input,))
t1.start()
t1.join()
t2.start()
t2.join()

print(complex(sum(list_fact)))




#print(factorial(1000000))

    