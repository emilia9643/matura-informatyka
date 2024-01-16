with open("liczby.txt") as file:
    data = file.read().split("\n")


def czyPalindrom(n):
    lista = list(str(n))
    length = len(lista)

    for i in range(length // 2):
        if lista[i] != lista[length - i - 1]:
            return False

    return True


for i in data:
    if i[-1] == "0":
        continue  # Skip the iteration if the number is "0"

    modified_number = int(i) + int(i[::-1])

    if czyPalindrom(modified_number):
        print(i)



