with open("programowanie/pi.txt", encoding="UTF-8") as file:
    data=file.read().split("\n")
fragmenty=[]

for i in range(0,len(data)-2):
    fragmenty.append(data[i]+data[i+1])


uni_fragmenty=sorted(set(fragmenty))

c={}

for i in uni_fragmenty:
    c.update({i:fragmenty.count(i)})

print(sorted(c.items(), key=lambda item: item[1])[0])
print(sorted(c.items(), key=lambda item: item[1])[len(c)-1])
