result = []


def divider(a, b):
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    return a/b


try:
    data = {10: 2, 15: 5, 8: 4, 32: 16, 30: 15, 300: 150}
    for key in data:
        res = divider(key, data[key])
        result.append(res)
except TypeError:
    print(".")

print(result)
