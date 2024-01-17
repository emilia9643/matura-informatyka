with open("Dane_PR/dane.txt") as file:
    data=[]
    for i in file.readlines():
        t=[]
        for y in i.strip("\n").split(" "):
            t.append(int(y))
        data.append(t)
file.close()

najdluzsza=0
for y in range(0,len(data[0])): #y na szerokosc |||| x na wysokosc
    obecny=0
    for x in range(0,len(data)-1):
        if data[x][y]==data[x+1][y]:
            obecny+=1
        else:
            if obecny>najdluzsza:
                najdluzsza=obecny
            obecny=0

print(najdluzsza+1)