def rozklad(liczba):
    o=[]
    for i in list(str(liczba)):
        o.append(int(i))
    return o

def liczbawesola(n):
    n=n
    poprzednie=[]
    while sum(rozklad(n))!=1:
        suma=0
        for i in rozklad(n):
            suma=suma+i*i
        if suma==1:
            return "Wesola"
        elif suma in poprzednie:
            return "Niewesola"
        else:
            n=suma
            poprzednie.append(suma)
    return "Wesola"
            
            
print(liczbawesola(85))

# print(sum(rozklad(10)))