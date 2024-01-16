with open("Dane_2212\mecz_przyklad.txt") as file:
    data=file.read()

punktyA=0
punktyB=0
for i in data:
    if i=="A":
        punktyA+=1
    else:
        punktyB+=1

    if (punktyA>=1000 or punktyB>=1000) and abs(punktyA-punktyB)>=3:
        print(f"A:{punktyA}, B:{punktyB}")
        punktyA=0
        punktyB=0
    else:
        pass

