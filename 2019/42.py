file=open("liczby.txt","r")
data=[]
for i in file.readlines():
    data.append(i.strip("\n"))

def silnia(a):
    if a==0:
        return 1
    else:
        o=1
        for i in range(1,a+1):
            o*=i
        return o

ile=0
cyfryWarunek=[]

for i in data:
    strCyfry=list(i)
    sumaSilni=0
    for y in strCyfry:
        sumaSilni+=silnia(int(y))
    if int(i)==sumaSilni:
        cyfryWarunek.append(int(i))
        ile+=1

print(ile)
print(cyfryWarunek)
