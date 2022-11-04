result = []
try:
    class BugOne(Exception):
        def __str__(self):
            return f"Number a must be bigger than b"

    class BugOne(Exception):
        def __str__(self):
            return f"Number a must be bigger than b"


    def divider(a, b):
        if a < b:
            raise ValueError(f"Number a must be bigger than b")
        if b > 100:
            raise IndexError(f"Number b can't be bigger than 100")
        return a/b


    data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8 : 4}
    for key in data:
        res = divider(key, data[key])
        result.append(res)
except TypeError:
    print("Uwu")

print(result)