file=open("przyklad.txt","r")
data=[]
for i in file.readlines():
    data.append(int(i.strip("\n")))

def nwd(a,b):
    pom=0
    while b!=0:
        pom=b
        b=a%b
        a=pom

    return a

dl=1
poczatek=0
datal=[]

for i in range(0,len(data)-2):
    if nwd(data[i],data[i+1])==nwd(data[i+1],data[i+2]) and nwd(data[i],data[i+1])>1:
        if dl==1:
            poczatek=i
            dl+=1
        else:
            dl+=1
    else:
        if dl>1:
            datal.append([dl+2,poczatek])
            dl=1
            poczatek=0

print(max(datal, key=lambda x: x[1]))
print(data[7])