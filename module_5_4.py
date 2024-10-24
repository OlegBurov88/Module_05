#   создаем класс House
class House:
    houses_history = []  # определяем атрибут класса

    #   определяем метод __new__
    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    #   определяем метод __init__
    def __init__(self, name, number_of_floors):
        self.name = name  # определяем атрибут имя
        self.number_of_floors = number_of_floors  # определяем атрибут кол-во этажей

    #   определяем метод go_to
    def go_to(self, new_floor):
        """
        Задаём условие, что выводим на экран значения от 1 до new_floor(включительно),
        только если new_floor меньше чем кол-во этажей или new_floor >= 1
        """
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)

    #   определяем метод __len__
    def __len__(self):
        return self.number_of_floors

    #   определяем метод __str__
    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    #   определяем метод __eq__
    def __eq__(self, other):
        if isinstance(other, House):  # проверяем параметр other на принадлежность к объекту типа House
            return self.number_of_floors == other.number_of_floors

    #   определяем метод __lt__
    def __lt__(self, other):
        if isinstance(other, House):  # проверяем параметр other на принадлежность к объекту типа House
            return self.number_of_floors < other.number_of_floors

    #   определяем метод __le__
    def __le__(self, other):
        if isinstance(other, House):  # проверяем параметр other на принадлежность к объекту типа House
            return self.number_of_floors <= other.number_of_floors

    #   определяем метод __gt__
    def __gt__(self, other):
        if isinstance(other, House):  # проверяем параметр other на принадлежность к объекту типа House
            return self.number_of_floors > other.number_of_floors

    #   определяем метод __ge__
    def __ge__(self, other):
        if isinstance(other, House):  # проверяем параметр other на принадлежность к объекту типа House
            return self.number_of_floors >= other.number_of_floors

    #   определяем метод __ne__
    def __ne__(self, other):
        if isinstance(other, House):  # проверяем параметр other на принадлежность к объекту типа House
            return self.number_of_floors != other.number_of_floors

    #   определяем метод __add__
    def __add__(self, value):
        if isinstance(value, int):  # проверяем параметр value на принадлежность к объекту типа int
            self.number_of_floors = self.number_of_floors + value
            return self

    #   определяем метод __radd__
    def __radd__(self, value):
        return self.__add__(value)

    #   определяем метод __iadd__
    def __iadd__(self, value):
        return self.__add__(value)

    #   определяем метод __del__
    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
