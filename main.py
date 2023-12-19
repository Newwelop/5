class Human:
    __height = 170
    _pole = 100
    group = "?????"

    def set_heigth(self, height):
        if height > 240:
            return
        self.__height = height

    def get_height(self):
        return self.__height

    def __method(self):
        print("Method")

class Student(Human):
    group = "1016"
    def __init__(self, height):
        self.set_heigth(height)


class Worker(Human):
    group = "Builder"



'''h = Human()
print(h.get_height())
h.set_heigth(175)
print(h.get_height())


stud = Student(160)
print(stud.get_height())
print(stud.group)

w = Worker()
print(w.get_height())
print(w.group)'''


class Comp:
    def __init__(self):
        super().__init__()
        self.memory = 128
    def calc(self):
        print("I`m calcing")

class Display:
    def __init__(self):
        super().__init__()
        self.resolution = "2k"
    def info(self):
        print("I`m printing info")


class Mobile(Comp, Display):
    def print_info(self):
        print(self.resolution)
        print(self.memory)


mob = Mobile()
mob.calc()
mob.info()
mob.print_info()