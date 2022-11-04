result = []


def divider(a, b):
    if a < b:
        raise BugOne()
    if b > 100:
        raise BugTwo()
    return a / b


class BugOne(Exception):
    def __str__(self):
        return f"Number a must be bigger than b"


class BugTwo(Exception):
    def __str__(self):
        return f"Number b can't be bigger than 100"


try:
    data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}
    for key in data:
        res = divider(key, data[key])
        result.append(res)
except TypeError as error:
    print(error)
print(result)

