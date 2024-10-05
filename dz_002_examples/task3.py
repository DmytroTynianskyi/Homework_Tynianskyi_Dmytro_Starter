# Завдання 3

# Створіть ієрархію класів із використанням множинного успадкування.
# Виведіть на екран порядок вирішення методів для кожного класу. Поясніть, чому лінеаризація даних класів виглядає саме так.

class A:
    def method(self):
        print("Метод класу A")


class B(A):
    def method(self):
        print("Метод класу B")


class C(A):
    def method(self):
        print("Метод класу C")


class D(B, C):
    pass


print(D.__mro__)

d = D()
d.method()



