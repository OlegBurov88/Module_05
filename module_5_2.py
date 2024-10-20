#   создаем класс House
class House:
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


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
