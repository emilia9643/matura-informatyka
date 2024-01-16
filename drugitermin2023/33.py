with open("przyklad.txt") as file:
    data=file.read().split("\n")

roznice=[]
for i in range(0,len(data)-2):
    roznice.append(
        abs(int(data[i],2) - int(data[i+1],2))
        )


print(bin(max(roznice))[2:])