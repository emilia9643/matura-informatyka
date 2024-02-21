data=[]
file=open("dane_obrazki.txt")
for i in file.read().split("\n\n"):
    obrazek1 = ""
    obrazek2 = ""
    obrazek3 = ""
    obrazek4 = ""
    for y in i.split("\n")[0:10]:
        obrazek1+=y[0:-1][0:10]
        obrazek2+=y[0:-1][10:20]
    for y in i.split("\n")[10:20]:
        obrazek3 += y[0:-1][0:10]
        obrazek4 += y[0:-1][10:20]
    data.append([obrazek1,obrazek2,obrazek3,obrazek4])
file.close()

ile=0

for i in data:
    if i.count(i[0])==4:
        ile+=1

print(ile)