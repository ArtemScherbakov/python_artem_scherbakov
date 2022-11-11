def raise_to_degrees(number, degree):
    i = 0
    for _ in range(degree):
        yield number**i
        i += 1


res = raise_to_degrees(123454, 500)
print(res)
for _ in res:
    print(_)
    print("----")