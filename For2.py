numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(len(numbers)):
    is_prime = True
    one = numbers[i]
    for k in range(1, one + 1):
        print(k)
        if one >= 2:
            c = one / k
            print(c)
    if one < 2:
        print(one, '- не простое и не сложное число')
        continue
def is_prime(numbers):
    if numbers <= 1:
        primes.append(numbers)
        return False
    for j in range(2, int(numbers ** 0.5) + 1):
        if numbers % i == 0:
            not_primes.append(is_prime)
            return False
        return True
print('Простые числа ', primes)
print('Составные числа', not_primes)

