class Book:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name.title()

    @name.setter
    def name(self, value):
        # Test Comment for Git
        self.__name = value.lower()


b = Book("slowness")
print(b.name)

b.name = "crim AND Punishment"
print(b.name)
