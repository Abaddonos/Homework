import random
def get_cipher():
    numbers = list(range(3, 21))
    cipher = random.choice(numbers)
    return cipher
n = get_cipher()
print('Шифр   :', n)
pairs = []
result = ''
for i in range(1, n):
    for j in range(1, n):
        if i >= j:
            continue
        else:
            kratno = n % (i + j)
            if kratno == 0 and i + j == n:
                pairs.append([i, j])
                result = result + str(i) + str(j)
print('Пары чисел', *pairs)
print('Пароль :', result,)