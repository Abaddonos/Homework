def calculate_structure_sum(data):
    total = 0
    for element in data:
        if isinstance(element, int): # Целые
            total += element
        elif isinstance(element, str): # Строки
            total += len(element)
        elif isinstance(element, (list, set, tuple)): # Листы, множества, кортежи
            total += calculate_structure_sum(element)
        elif isinstance(element, dict): # Списки
            for key, value in element.items():
                total += calculate_structure_sum([key, value])
    return total
data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)  # Ожидаемый вывод: 99