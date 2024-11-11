#https://github.com/Abaddonos/Homework/blob/detached2/Class.py
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        stroka = str(f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')
        return stroka
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
# __str__
print(h1)
print(h2)
# __len__
print(len(h1))
print(len(h2))