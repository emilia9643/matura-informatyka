with open("liczby.txt") as file:
    data=[]
    for i in file.read().split("\n"):
        data.append(int(i))
file.close()

mniejszeniz1000=[]
for i in data:
    if i<1000:
        mniejszeniz1000.append(i)

print(mniejszeniz1000[-2])
print(mniejszeniz1000[-1])
print(len(mniejszeniz1000))