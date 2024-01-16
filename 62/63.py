with open("liczby1.txt") as file:
    temp=file.read().split("\n")
    data1=[]
    for i in temp:
        data1.append(int(i,8))
file.close()
with open("liczby2.txt") as file:
    temp=file.read().split("\n")
    data2=[]
    for i in temp:
        data2.append(int(i))
file.close()

ilerownych=0
ilewiekszychw1=0

for i in range(0,1000):
    if data1[i]==data2[i]:
        ilerownych+=1
    elif data1[i]>data2[i]:
        ilewiekszychw1+=1
    else:
        continue

print(ilerownych)
print(ilewiekszychw1)