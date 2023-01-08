def suma_recursiva(a,b):
    if b == 0:
        return a

    else:
        return 1+suma_recursiva(a,b-1)
    
print(suma_recursiva(2,8))