with open("liczby.txt") as file:
    data=[]
    for i in file.read().split("\n"):
        data.append(int(i))
file.close()

liczbydzielniki={

}

for a in data:
    dzielniki=frozenset({})
    for i in range(2,a//2+1):
        if a%i==0:
            dzielniki=dzielniki.union({i})
        else:
            continue     
    liczbydzielniki.update({a:dzielniki})

for i in liczbydzielniki.items():
    ile=0
    for y in liczbydzielniki.items():
        if i[1]&y[1]:
            ile+=1
        else:
            continue
    if ile==1:
        print(i[0])



