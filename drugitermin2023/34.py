with open("anagram.txt") as file:
    data=file.read().split("\n")

dziesietne=[]
for i in data:
    dziesietne.append(int(i,2))

# ilebezzer=0
# for i in dziesietne:
#     if str(i).count("0")==0:
#         ilebezzer+=1
#     else:
#         pass

# print(ilebezzer)

sumycyfr={}

for i in dziesietne:
    pierwotna=i
    suma=0
    rozne=set(str(i))
    for i in rozne:
        suma+=int(i)
    sumycyfr.update({pierwotna:suma})

print(max(sumycyfr.values()))

