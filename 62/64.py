with open("liczby2.txt") as file:
    temp=file.read().split("\n")
    data1=[]
    for i in temp:
        data1.append(i)

ile6=0
ile6w8=0
for i in data1:
    ile6+=i.count("6")
    ile6w8+=oct(int(i))[2:].count("6")

print(ile6)
print(ile6w8)