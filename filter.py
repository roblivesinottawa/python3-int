def positives():
    num = []
    for n in range(-10, 10):
        if n > 0:
            num.append(n)
    return num

print(positives())

nums = range(-10, 10)
positive = list(filter(lambda  n : n > 0, nums))
print(positive)


def odds():
    odd_numbers = []
    for odd in range(-10, 10):
        if odd % 2 != 0:
            odd_numbers.append(odd)
    return odd_numbers

print(odds())

odds = list(filter(lambda n : n % 2 != 0, nums))
print(odds)


def evens():
    even_nums = []
    for even in range(-10, 10):
        if even % 2 == 0:
            even_nums.append(even)
    return even_nums

print(evens())
evens = list(filter(lambda n : n % 2 == 0, nums))
print(evens)




def negatives():
    n = []
    for num in range(-10, 10):
        if num < 0:
            n.append(num)
    return n

print(negatives())

nums = range(-10, 10)

negative = list(filter(lambda x: x < 0, nums))
print(negative)

