with open("Dane_PR/dane.txt") as file:
    data=[]
    for i in file.readlines():
        t=[]
        for y in i.strip("\n").split(" "):
            t.append(int(y))
        data.append(t)
file.close()

kontrast=0

for i in range(0,len(data)-1):
    for y in range(0,len(data[0])-1):
        if abs(data[i][y]-data[i+1][y])>128:
            kontrast+=1
        if abs(data[i][y]-data[i][y+1])>128:
            kontrast+=1


print(kontrast)