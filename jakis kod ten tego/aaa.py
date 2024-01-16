# tablica=["(-10,5>","(6,11)","<11,20>"]
#
# suma=[]
#
#
# for i in tablica:
#     if tablica[0][0] == "(":
#         od = int(i[1:i.find(",")]) + 1
#     else:
#         od = int(i[1:i.find(",")])
#
#     if tablica[0][-1] == ")":
#         do = int(i[i.find(",") + 1:len(i) - 1]) - 1
#     else:
#         do = int(i[i.find(",") + 1:len(i) - 1])
#
#     liczby=[]
#     for z in range(od, do+1):
#         liczby.append(z)
#
#     suma+=liczby
#
# print(suma)

print(int("F5785",16))