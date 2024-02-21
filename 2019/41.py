file=open("liczby.txt","r")
data=[]
for i in file.readlines():
    data.append(int(i.strip("\n")))

potegi3=[]
y=3
potega=0
while pow(3,potega)<100000:
    potegi3.append(pow(3,potega))
    potega+=1

ile=0

for i in data:
    if i in potegi3:
        ile+=1

print(ile)
# 18