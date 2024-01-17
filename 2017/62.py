with open("Dane_PR/dane.txt") as file:
    data=[]
    for i in file.readlines():
        t=[]
        for y in i.strip("\n").split(" "):
            t.append(int(y))
        data.append(t)
file.close()

def isSymetrical(a):
    for i in range(0,len(a)//2+2):
        if a[i]==a[319-i]:
            continue
        else:
            return False
    return True

ileZle=0

for i in data:
    if isSymetrical(i)==True:
        continue
    else:
        ileZle+=1

print(ileZle) #149