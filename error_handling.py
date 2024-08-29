def divide(a: int, b: int) -> float:
    result = None
    try:
        result: float = a / b
    except ZeroDivisionError as exc:
        print("Invalid input by Peyman")
        print(exc)
    except IndexError:
        print("Invalid index")
    finally:
        print("Finally block")
    return result


result = divide(1, 0)


# for i in range(10):
#     x = i + 2
#     print(x)
