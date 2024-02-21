data=[]
file=open("dane_obrazki.txt")
for i in file.read().split("\n\n"):
    obrazek=[]
    bityRows=[]
    bityColumns=[]
    for y in i.split("\n")[0:-1]:
        obrazek.append(y[0:-1])
    for y in i.split("\n")[0:-1]:
        bityRows.append(y[-1])
    for y in i.split("\n")[-1]:
        bityColumns.append(y)
    data.append([obrazek,bityRows,bityColumns])
file.close()


output=[]

for z in data:
    ilezleRows=0
    ilezleColumns=0
    for i in range(0,20):
        if z[0][i].count("1")%2!=int(z[1][i]):
            ilezleRows+=1

    for i in range(0,20):
        column=""
        for y in range(0,20):
            column+=z[0][y][i]
        if column.count("1")%2!=int(z[2][i]):
            ilezleColumns+=1


    if ilezleRows+ilezleRows==0:
        output.append("poprawny")
        pass
    elif ilezleColumns==1 or ilezleRows==1:
        output.append("naprawialny")
        pass
    else:
        output.append("nienaprawialny")
        pass

print(output.count("poprawny"))
print(output.count("naprawialny"))
print(output.count("nienaprawialny"))