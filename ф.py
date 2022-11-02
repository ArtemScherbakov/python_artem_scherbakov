import random

def Bug(a, b):
    if a > b:
        raise f"Bug. Ти повинен ввести спочатку менше число."
    else:
        print(random.randint(a, b))


a = int(input("Введіть число: "))
b = int(input("Введіть число: "))


Bug(a, b)

