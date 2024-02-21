def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

with open("ciagi.txt") as file:
    data = file.read().split("\n")

ile = 0

for line in data:
    try:
        a = int(line, 2)
        if is_prime(a):
            ile += 1
    except ValueError:
        # Handle the case where the line is not a valid binary representation
        pass

print(ile)
