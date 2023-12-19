class Human:
    __height = 170
    pole = 100
    group = "?????"

def set_height(self, height):
    if height > 240:
        return
    self.__height = height

def get_height(self):
    self.__method()
    return self.__height






    def __method(self):
        print("method")


class Student(Human):
    group = "1016"

    def __init__(self, height):
       return self.__height



class Worker(Human):
    group = "Builder"

h = Human()
print(h.get_height())

stud = Student(160)
print(stud.height)
print(stud.group)


w = Worker()
print(w.height)
print(w.group)
