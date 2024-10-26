class Database:
    """
    Класс базы данных содержащий: логин, пароль
    """

    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    """
    Класс пользователя, содержащий атрибуты: логин, пароль
    """

    def __init__(self, username, password, password_confirm):
        self.username = username
        self.password = password


if __name__ == '__main__':
    database = Database()
    while True:
        choice = input('\nПриветствуем! Выберите действие: \n1 - Вход\n2 - Регистрация\nВведите 1 или 2: ')
        if choice == '1':
            login = input('Введите логин: ')
            if login in database.data:
                password_0 = input('Введите пароль: ')
                if password_0 == database.data[login]:
                    print(f'Вход выполнен, {login}')
                    break
                else:
                    print('Неверный пароль')
            else:
                print('Такого пользователя не существует.')

        if choice == '2':
            user_01 = User(input('Введите логин: '),
                           password_1 := input('Введите пароль: '),
                           password_2 := input('Повторите пароль: '))
            if password_1 != password_2:
                print('Пароли не совпадают, попробуйте ещё раз.')
                continue
            elif password_1 == password_2:
                contains_a_digit = False
                contains_a_caps = False
                for i in password_1:
                    if i.isnumeric():
                        contains_a_digit = True
                    if i.isupper():
                        contains_a_caps = True
                if contains_a_caps and contains_a_digit:
                    database.add_user(user_01.username, user_01.password)
                else:
                    print('Пароль не соответствует требованиям, попробуйте ещё раз.')
                    continue

        print(database.data)
