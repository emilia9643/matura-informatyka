with open("ciagi.txt") as file:
    data=file.read().split("\n")

def czyDwucykliczny(a):
    if len(a)%2!=0:
        return False
    else:
        w=len(a)
        if a[0:w//2]==a[w//2:]:
            return True
        else:
            return False

ile=0

for i in data:
    if czyDwucykliczny(i)==True:
        ile+=1
    else:
        pass

print(ile)