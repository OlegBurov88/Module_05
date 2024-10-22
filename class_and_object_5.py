class Human:

    head = True

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

    def __lt__(self, other):
        return self.age < other.age

    def __gt__(self, other):
        return self.age > other.age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __bool__(self):
        return bool(self.age)

    def __str__(self):
        return f'{self.name}'

    def __del__(self):
        print(f'{self.name} ушёл')


den = Human('Денис', 22)
max_ = Human('Макс', 22)

a = 6
print(Human.head)
print(Human.__dict__)
print(den.__dict__)
Human.head = False

print(den.__dict__)
den.head = True
print(den.__dict__)
print(max_.__dict__)
print(max_.head)