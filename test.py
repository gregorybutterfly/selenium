
class Age:

    def age(self):
        return 5


class Name:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.age = Age.age(self)

c = Name('Adam', 'Malysz')

print(c.age)