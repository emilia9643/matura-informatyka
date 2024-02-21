data=[]
file=open("dane_obrazki.txt")
for i in file.read().split("\n\n"):
    obrazek=""
    for y in i.split("\n")[0:-1]:
        obrazek+=y[0:-1]
    data.append(obrazek)
file.close()

rewersy=0
ileCzarnych=[]

for i in data:
    if i.count("1")>i.count("0"):
        ileCzarnych.append(i.count("1"))
        rewersy+=1

print(rewersy)
print(max(ileCzarnych))