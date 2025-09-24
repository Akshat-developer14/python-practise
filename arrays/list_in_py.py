'''

1. Python Lists (most common “array-like” structure)

- Flexible, built-in sequence type.
- Can hold mixed data types (e.g., integers, strings, objects).
- Dynamically resizable (no need to declare size).
- Tons of built-in methods (append, remove, sort, etc.).

'''

# list
list1 = [1, 2, 3, 4, 5]
print('list1: ',list1)  # [1, 2, 3, 4, 5]
print('list1[0]: ',list1[0])  # 1
print('list1[1:3]: ',list1[1:3])  # [2, 3]
print('list1[-1]: ',list1[-1])  # 5
print('list1[::-1]: ',list1[::-1])  # [5, 4, 3, 2, 1]

list1.append(6)  # [1, 2, 3, 4, 5, 6]
print('list1.append(6): ',list1)  # [1, 2, 3, 4, 5, 6]

list1.pop()  # [1, 2, 3, 4, 5]
print('list1.pop(): ',list1)  # [1, 2, 3, 4, 5]

# insert(index, value)
list1.insert(0, 0)  # [0, 1, 2, 3, 4, 5]
print('list1.insert(0, 0): ',list1)  # [0, 1, 2, 3, 4, 5]

# remove(value)
list1.remove(0)  # [1, 2, 3, 4, 5]
print('list1.remove(0): ',list1)  # [1, 2, 3, 4, 5]

list2 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]


# sort()
list2.sort()  # [1, 2, 3, 4, 5]
print('list2.sort(): ',list2)  # [1, 2, 3, 4, 5]

# reverse()
list1.reverse()  # [5, 4, 3, 2, 1]
print('list1.reverse(): ',list1)  # [5, 4, 3, 2, 1]

# clear()
list1.clear()  # []
print('list1.clear(): ',list1)  # []