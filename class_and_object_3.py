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

    def __len__(self):
        return self.age

    def __del__(self):
        print(f'{self.name} ушёл')


den = Human('Денис', 22)
max_ = Human('Макс', 25)
max_.birthday()

print(len(den))

del den

input()