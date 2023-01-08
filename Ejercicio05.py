import time

def fibonacci_recursivo(n): 
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    else:
        return fibonacci_recursivo(n-1)+fibonacci_recursivo(n-2)

tiempo_1=time.perf_counter()
print(fibonacci_recursivo(5))
tiempo_2=time.perf_counter()
print("fibonacci recursivo se hizo en el tiempo",tiempo_2-tiempo_1)


def fibonacci(num):
    if num==0 or num==1:
        return num
    
    a = 0
    b = 1
    for i in range(1,num+1):
        c = b+a
        a = b
        b = c
    return a

tiempo_1=time.perf_counter()
print(fibonacci(5))
tiempo_2=time.perf_counter()
print("fibonacci recursivo se hizo en el tiempo",tiempo_2-tiempo_1)