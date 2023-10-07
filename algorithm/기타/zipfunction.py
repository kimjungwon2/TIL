date = [1, 2, 3, 4, 5]
letter = ['영희', '철수', '희동', '희루', '아용']

for i in zip(date, letter):
    print(i)

pairs = list(zip(date, letter))

print(pairs)

a, b = zip(*pairs)

print(a)
print(b)


keys = ["1", "2", "3"]
value = ["g", "f", "k"]

print(dict(zip(keys, value)))
