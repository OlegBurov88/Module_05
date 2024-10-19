class Human:
    def __init__(self, name):
        self.name = name


den = Human('Денис')
max_ = Human('Макс')

print(type(den))
print(den == max_)
print(den is max_)
print(id(den), id(max_))
print(den.name, max_.name)
