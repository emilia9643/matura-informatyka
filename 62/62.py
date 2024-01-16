with open("liczby2.txt") as file:
    temp=file.read().split("\n")
    data=[]
    for i in temp:
        data.append(int(i))
file.close()

dl=1
pierwszy=0
najdluzszy=0
poczateknajdluzszy=0

for i in range(0,len(data)-1):
    if data[i+1]-data[i]>=0:
        if dl==1:
            pierwszy=data[i]
        dl+=1
    else:
        if dl>najdluzszy:
            poczateknajdluzszy=pierwszy
            najdluzszy=dl
        dl=1

print(najdluzszy)
print(poczateknajdluzszy)