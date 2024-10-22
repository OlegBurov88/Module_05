print(int.__mro__)
print(object)


class User:
    __instance = None

    def __new__(cls, *args, **kwargs):
        print('Я в нью')
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, *args, **kwargs):
        print('Я в ините')
        self.args = args
        self.kwargs = kwargs
        for key, value in kwargs.items():
            setattr(self, key, value)


other = [1, 2, 3]
user = {'name': 'Den', 'age': 25, 'gender': 'male'}

user1 = User()
user2 = User()
print(User.__mro__)
print(user1)
print(id(user1), id(user2))

user1 = User(*other, **user)
print(user1.args)
print(user1.kwargs)
print(user1.name, user1.age, user1.gender)
