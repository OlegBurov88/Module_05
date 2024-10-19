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


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)

#   свои данные для проверки
print()
h3 = House('Ярославский', 22)
print(h3.name, h3.number_of_floors)
h3.go_to(1)
h3.go_to(18)
h3.go_to(-1)
