test1 = [1, 2, 3, 4, 5]

test1.insert(1, 2)

print(test1)

test1.clear()

print(test1)
test1 = [1, 2, 3, 4, 5, 5, 6]

del (test1[3])

print(test1)

test1.pop()
print(test1)

num = test1.count(5)

print(num)

test2 = test1.copy()
print(test2)

test2 = [10, 11, 12]

test1.extend(test2)

print(test1)

test3 = sorted(test1, reverse=True)
print(test3)
