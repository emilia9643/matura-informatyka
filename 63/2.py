with open("ciagi.txt") as file:
    data=file.read().split("\n")
file.close()

ile=0
def czyWarunek(a):
    for y in range(0,len(a)-1):
        if a[y]==a[y+1] and a[y]=="1" and a[y+1]=="1":
            return False
    return True

for i in data:
    if czyWarunek(i)==True:
        ile+=1
    else:
        pass

print(ile) #93