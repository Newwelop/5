class A:
    def __init__(self, a):
        self.a = a

    def method_a(self):
        print("Метод из А")

class B:
    def __init__(self, b):
        self.b = b

    def method_b(self):
        print("Метод из Б")

class ComplexClass(A, B):
    def __init__(self, a, b):
        A.__init__(self, a)
        B.__init__(self, b)



