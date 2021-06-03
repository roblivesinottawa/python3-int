# compute the product of a list of integers

# product = 1
# list_ = [1,2,3,4,5,6,7,8]
# for n in list_:
#     product *= n
#     print(f"product of {n} is: {product}")



from functools import reduce

list_ = [1,2,3,4,5,6,7,8]
product = reduce((lambda x, y: x * y), list_)
print(product)