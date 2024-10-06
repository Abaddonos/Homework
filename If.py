first = int(input('Введите число первое число: '))
second = int(input('Введите число второе число: '))
thirt = int(input('Введите число третье число: '))
if first == second and second == thirt:
    print('3')
elif first == second or second == thirt or first == thirt:
    print('2')
else:
    print('0')
