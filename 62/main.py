with open("liczby1.txt") as file:
    temp=file.read().split("\n")
    data=[]
    for i in temp:
        data.append(int(i,8))
file.close()

print(oct(min(data))[2:])
print(oct(max(data))[2:])