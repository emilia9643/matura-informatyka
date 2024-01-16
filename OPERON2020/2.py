with open("dane.txt") as file:
    data=file.read().split("\n")

numbers=[]
happy=[1,3]
for i in range(1,10000,2):
    numbers.append(i)
while len(numbers)>happy[-1]:
    delete=[]
    for i in range(happy[-1]-1,len(numbers),happy[-1]):
        delete.append(numbers[i])
    for i in delete:
        numbers.remove(i)

    happy.append(numbers[len(happy)])

ileszczesliwych=0
for i in set(data):
    if happy.count(int(i))>0:
        ileszczesliwych=ileszczesliwych+1
    else:
        pass
print(happy)