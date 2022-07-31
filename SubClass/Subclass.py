class A:
    def __init__(self, value_of_zero):
        self.pi = 3.14
        self.e = 2.7
        print(value_of_zero)

    def multiply(self, a, b):
        return a*b

MATH = A(value_of_zero=0)
print(MATH.pi)
print(MATH.multiply(2, MATH.pi))


class B(A):
    def square(self, value):
        return self.multiply(value, value)

SUBCLASS = B(0)
print(SUBCLASS.square(int(input("Input"))))