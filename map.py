"""map applies a function to all the items in an input list"""

# regular way using append
items = [10, 20, 30, 40, 50]
squared = []
for n in items:
    squared.append(n ** 2)

print(squared)

# with map:
items_ = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, items_))
print(squared)
