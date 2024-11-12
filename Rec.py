def get_multiplied_digits(number):
    number = int(number)
    str_number = str(number)
    first = int(str_number[0])
    while str_number.endswith('0'):
        str_number = str_number[:len(str_number) - 1]
    if len(str_number) <= 1:
        return first
    else:
        return first * get_multiplied_digits(int(str_number[1:]))
result = get_multiplied_digits('096085020')
print(result)