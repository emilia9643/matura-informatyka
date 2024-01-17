with open("Dane_PR/dane.txt") as file:
    data=[]
    for i in file.readlines():
        i.strip("\n")
        for y in i.split(" "):
            data.append(int(y))


file.close()
print(max(data)) #221
print(min(data)) #7