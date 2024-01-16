with open("przyklad.txt") as file:
    data=file.read().split("\n")

def silnia(n):
    r=1
    for i in range(1,n+1):
        r*=i
    return r

def S(n,k):
    return int(silnia(n)/(silnia(k)*silnia(n-k)))

osmiocyfrowe=[]

for i in data:
    if len(i)==8:
        osmiocyfrowe.append(i)

results={}

for i in osmiocyfrowe:
    results.update({i:int(S(8, i.count("0")) * S(8 - i.count("0") - 1, i.count("1") - 1))})

print(results)





