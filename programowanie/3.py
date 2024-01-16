# with open("programowanie/pi_przyklad.txt", encoding="UTF-8") as file:
#     data=file.read().split("\n")


def czywzrasta(a):
    ostatnia=a[0]
    rosnie=True
    maleje=False
    stala=0
    wzrosla=0
    zmalala=0
    for i in range(1,len(a)):
        if rosnie==True and maleje==True and stala>1:
            return False
        if a[i-1]<a[i]:
            rosnie=True
            maleje=False
            wzrosla=1
        elif a[i-1]==a[i]:
            rosnie=True
            maleje=True
            stala=stala+1
        elif a[i-1]>a[i]:
            maleje=True
            rosnie=False
            zmalala=1
            
        if wzrosla>1 or zmalala>1:
            return False

 
    return True

print(czywzrasta([0,2,8,8,4,1,4]))

