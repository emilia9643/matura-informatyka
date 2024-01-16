import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def count_numbers_with_three_odd_prime_factors(filename):
    with open(filename) as file:
        data = [line.strip() for line in file if line.strip()]

    def get_prime_factors_count(number):
        factors = set()
        for i in range(2, int(math.sqrt(number)) + 1):
            while number % i == 0 and is_prime(i):
                factors.add(i)
                number //= i
        if number > 1 and is_prime(number):
            factors.add(number)
        return factors

    count = 0
    for item in data:
        try:
            number = int(item)
            prime_factors = get_prime_factors_count(number)
            if len(prime_factors) == 3 and all(factor % 2 == 1 for factor in prime_factors):
                count += 1
        except ValueError:
            print(f"Skipping invalid input: {item}")

    return count

result = count_numbers_with_three_odd_prime_factors("liczby.txt")
print(result)