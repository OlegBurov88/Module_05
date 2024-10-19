class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.say_info()

    def say_info(self):
        print(f'Привет, меня зовут {self.name}, мне {self.age}')

    def birthday(self):
        self.age += 1
        print(f'У меня день рождения, мне теперь {self.age}')


den = Human('Денис', 22)
max_ = Human('Макс', 25)

print(den.name, den.age)
print(max_.name, max_.age)

den.surname = 'Попов'
den.age = 23
print(den.surname, den.name, den.age)

den.say_info()
max_.say_info()

max_.birthday()
