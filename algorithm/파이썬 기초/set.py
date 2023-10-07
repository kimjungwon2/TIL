data = set([1, 1, 2, 3, 4, 4, 5, 5, 5, 5])

b = set([3, 4, 5, 6, 6, 7])

print(data | b)
print(data & b)
print(data-b)

data.add(9)
print(data)

data.update([5,6,8])
print(data)

data.remove(5)

print(data)
