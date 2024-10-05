immutable_var = 'String', 1999, True
print(immutable_var)
new_age = immutable_var[1] + 1
new_string = immutable_var[0] + ' number 1'
print(new_age)
print(new_string)
print(type(immutable_var))
# immutable_var[2] = False TypeError: 'tuple' object does not support item assignment
mutable_list = ['red', 2000, False]
print(mutable_list)
mutable_list[0] = 'blue'
print(mutable_list)
print(type(mutable_list))
mutable_list.extend(['black', 5000])
print(mutable_list)
print(mutable_list[3])
print(mutable_list[::-1])
print('Mutable List:', mutable_list[::-1])
print('Immutable Var:', immutable_var)
