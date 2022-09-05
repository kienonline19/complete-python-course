"""
class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        print("Called static_method")


# obj = ClassTest()
# obj.instance_method()
# ClassTest.instance_method(obj)
ClassTest.class_method()
"""
class Book:
    TYPES = ('hardcover', 'paperback')

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"


# print(Book.TYPES)
# book = Book('Harry Potter', 'hardcover', 1500)
# print(book)

book = Book.hardcover("Doremon", 1500)
light = Book.paperback("Conan", 600)

print(book)
print(light)
