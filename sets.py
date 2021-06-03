list_nums = [2, 4, 5, 8, 9, 2, 10, 4, 8]

duplicates = []
for v in list_nums:
    if list_nums.count(v) > 1:
        if v not in duplicates:
            duplicates.append(v)

print(duplicates)

another_list = ['a', 'b', 'c', 'a', 'd', 'e', 'c']
duplicates_ = set([x for x in another_list if another_list.count(x) > 1])
print(duplicates_)