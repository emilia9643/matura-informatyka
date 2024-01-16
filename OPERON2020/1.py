with open("dane.txt") as file:
    data=file.read().split("\n")

szczesliwe=[1,3]
liczby=[]
for i in range(1,10000,2):
    liczby.append(i)

while szczesliwe[-1]<len(liczby):
    dlpierwotna=len(liczby)
    ostatniaszczesliwa=szczesliwe[-1]
    delete=[]
    for i in range(ostatniaszczesliwa-1,dlpierwotna-1,ostatniaszczesliwa):
        delete.append(liczby[i])
    for i in delete:
        liczby.remove(i)
    szczesliwe.append(liczby[len(szczesliwe)])

ileszczesliwych=0
for i in set(data):
    if liczby.count(int(i))>0:
        ileszczesliwych=ileszczesliwych+1
    else:
        pass


print(ileszczesliwych)
