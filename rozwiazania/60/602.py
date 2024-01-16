with open("liczby.txt") as file:
    data=[]
    for i in file.read().split("\n"):
        data.append(int(i))
file.close()

def iledzielnikow(a):
    ile=2
    dzielniki=[1]
    for i in range(2,a//2+1):
        if a%i==0:
            ile+=1
            dzielniki.append(i)
        else:
            continue
    dzielniki.append(a)
    return (ile,dzielniki)

for i in data:
    if iledzielnikow(i)[0]==18:
        print(i)
        print(iledzielnikow(i)[1])
    else:
        continue
