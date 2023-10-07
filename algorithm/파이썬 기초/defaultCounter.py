from collections import defaultdict, Counter

a = defaultdict(int)

a['A'] = 5
a['B'] = 4
print(a)

a['C'] += 1
print(a)


a_list = [1, 2, 3, 4, 5, 5, 5, 6, 6, 7]
b = Counter(a_list)

print(b)

print(b.most_common(1)[0][0])
