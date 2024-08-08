def hello_decorator(func):
    def inner1(*args, **kwargs):
        print("before execute func", args, kwargs)
        returned_value = func(*args, **kwargs)
        print("after execute func", returned_value)
        return returned_value

    return inner1


@hello_decorator
def sum_to_numbers(a, b):
    print("함수 실행 중")
    return a + b


print("두 수의 합 => ", sum_to_numbers(3, 5))
