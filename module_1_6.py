my_dict = {'Abbos': 1999, 'Yaroslav': 2000}
print('Dict:', my_dict)
print('Existing value:', my_dict.get('Abbos'))
print('Not existing value:', my_dict.get('Petr'))
my_dict.update({'Marina': 2001, 'Alexandr': 2001})
deleted_value = my_dict.pop('Yaroslav')
print('Deleted value:', deleted_value)
print('Modified dictionary:', my_dict)
my_set = {1999, 2000, 2001, 1999, 'Abbos', 'Yaroslav', 'Abbos', 2001, True, True}
print("\n"'Set:', my_set)
my_set.update([2003, 'Marina', 'Marina'])
my_set.remove(2000)
print('Modified set:', my_set)
