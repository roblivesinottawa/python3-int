def multiply(n):
    return n * n

def add(n):
    return n + n
#
# def subtract(n):
#     return n - n

functions = [multiply, add]
for x in range(10):
    value = list(map(lambda n:n(x), functions))
    print(value)
