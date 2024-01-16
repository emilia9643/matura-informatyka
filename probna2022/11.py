with open("Dane_2212\mecz_przyklad.txt") as file:
    data=file.read()

ilezmian=0
for i in range(1,len(data)-1):
    if data[i-1]==data[i]:
        pass
    else:
        ilezmian+=1

print(ilezmian)