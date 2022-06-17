import functools


def memory(func):
    calculated = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args in calculated:
            return calculated[args]
        else:
            val = func(*args)
            calculated[args] = val
            return val
    return wrapper


@memory
def fibonacci(n):
    return n if 0 <= n < 2 else fibonacci(n - 1) + fibonacci(n - 2)


for i in range(100):
    print(fibonacci(i))
