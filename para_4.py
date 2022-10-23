class Human:
    height = 170


class Student(Human):
    pass


class Worker(Human):
    pass


artem = Student()
alex = Worker()
taya = Student()

print(artem.height)
print(alex.height)
print(taya.height)

