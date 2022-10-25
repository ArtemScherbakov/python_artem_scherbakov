class Man:
    height = 180
    weight = 80
    gender = "Male"

    def __init__(self):
        self.height = 170
        self.weight = 65
        self.gender = "Male"


class Woman:
    height = 160
    weight = 55
    gender = "Female"

    def __init__(self):
        self.height = 155
        self.weight = 45
        self.gender = "Female"


class Child:
    year = 15


class Adults:
    year = 35


class Elderly:
    year = 70


class Student:
    college = True
    knowledge = 50
    money = 50


class Worker:
    knowledge = 100
    money = 100
    work = True


class Pensioner:
    knowledge = 125
    money = 75


class Dad(Man, Worker, Adults):
    def __init__(self):
        super().__init__()
        print(f"Dad height is {super().height} cm")
        print(f"Dad weight is {super().weight} kg")
        print(f"Dad is {self.year} years old")
        print(f"Dad gender is {self.gender}")
        print(f"Dad has work? - {self.work}")
        print(f"Dad salary is {self.money} $")
        print(f"Dad knowledge is {self.knowledge}")


class Son(Man, Student, Child):
    def __init__(self):
        super().__init__()
        print(f"Son height is {self.height} cm")
        print(f"Son weight is {self.weight} kg")
        print(f"Son is {self.year} years old")
        print(f"Son gender is {self.gender}")
        print(f"Son has college? - {self.college}")
        print(f"Son scholarship is {self.money} $")
        print(f"Son knowledge is {self.knowledge}")


class Mother(Woman, Worker, Adults):
    def __init__(self):
        super().__init__()
        print(f"Mother height is {super().height} cm")
        print(f"Mother weight is {super().weight} kg")
        print(f"Mother is {self.year} years old")
        print(f"Mother gender is {self.gender}")
        print(f"Mother has work? - {self.work}")
        print(f"Mother salary is {self.money} $")
        print(f"Mother knowledge is {self.knowledge}")


class Daughter(Woman, Student, Child):
    def __init__(self):
        super().__init__()
        print(f"Daughter height is {self.height} cm")
        print(f"Daughter weight is {self.weight} kg")
        print(f"Daughter is {self.year} years old")
        print(f"Daughter gender is {self.gender}")
        print(f"Daughter has college? - {self.college}")
        print(f"Daughter scholarship is {self.money} $")
        print(f"Daughter knowledge is {self.knowledge}")


class Grandfather(Man, Pensioner, Elderly):
    def __init__(self):
        super().__init__()
        print(f"Grandfather height is {super().height} cm")
        print(f"Grandfather weight is {super().weight} kg")
        print(f"Grandfather is {self.year} years old")
        print(f"Grandfather gender is {self.gender}")
        print(f"Grandfather pension is {self.money} $")
        print(f"Grandfather knowledge is {self.knowledge}")


class Grandmother(Woman, Pensioner, Elderly):
    def __init__(self):
        super().__init__()
        print(f"Grandmother height is {super().height} cm")
        print(f"Grandmother weight is {super().weight} kg")
        print(f"Grandmother is {self.year} years old")
        print(f"Grandmother gender is {self.gender}")
        print(f"Grandmother pension is {self.money} $")
        print(f"Grandmother knowledge is {self.knowledge}")


print("______Dad______")
dima = Dad()
print("______Son______")
vasya = Son()
print("______Mother______")
vika = Mother()
print("______Daughter______")
liza = Daughter()
print("______Grandfather______")
peter = Grandfather()
print("______Grandmother______")
anna = Grandmother()
