def potencia(a,b):
    if b==1:
        return a
    else:
        if b % 2 == 0:
            c  = potencia(a,(b/a))
            return c*c
        
        return a*potencia(a,b-1)
print(potencia(2,2))