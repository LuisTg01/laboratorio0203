import time


def recursivo_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursivo_factorial(n-1)

tiempo_1=time.perf_counter()
print(recursivo_factorial(8))
tiempo_2=time.perf_counter()
print("El factorial se resolvió en el tiempo",tiempo_2-tiempo_1)


def factorial(n):
    producto = 1
    for i in range(1,n+1):
        producto = producto * i

    return producto

tiempo_1=time.perf_counter()
print(factorial(8))
tiempo_2=time.perf_counter()
print("El factorial se resolvió en el tiempo",tiempo_2-tiempo_1)