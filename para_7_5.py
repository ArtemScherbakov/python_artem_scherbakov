def checker(function):
    def checker(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
        except Exception as exc:
            print(f"We have problem {exc}")
        else:
            print(f"No problem, Result - {result}")
    return checker


def calc(expression):
    return eval(expression)


calc = checker(calc)
calc("b*a")