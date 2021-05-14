def gen():
    """generators are iterators that can iterate over just once"""
    for x in range(20):
        yield x


for item in gen():
    print(item)

# a better use is when calculating large sets of numbers


# def fibonacci(n):
#     a = b = 1
#     for x in range(n):
#         yield a
#         a, b = b, a + b


# for i in fibonacci(100):
#     print(i)


def fib(num):
    a = b = 1
    result = []
    for x in range(num):
        result.append(a)
        a, b = b, a + b
    return result


for i in fib(10):
    print(i)
