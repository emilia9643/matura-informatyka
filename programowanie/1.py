suma=0

for i in range(1,1000000):
    t=str(i)
    zapisbinarny=bin(i)[2:]
    if t==t[::-1] and zapisbinarny==zapisbinarny[::-1]:
        suma=suma+i
        print(i)
    else:
        suma=suma+0


print(suma)

