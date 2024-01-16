with open("przyklad.txt") as file:
    data=file.read().split("\n")

zrownowazone=0
prawie=0

for i in data:
    zera=i.count("0")
    jedynki=i.count("1")
    if zera==jedynki:
        zrownowazone+=1
    elif abs(zera-jedynki)==1:
        prawie+=1
    else:
        pass

print(zrownowazone)
print(prawie)