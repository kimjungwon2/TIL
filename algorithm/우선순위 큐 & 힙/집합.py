a = set()

a.add(3)
a.add(5)

a.add(6)
a.add(3)

for i in a:
    print(i)

a.remove(3)

print(a)

s = dict()

s[1] = 'hello'
s[2] = 1
s['he'] = 'she'
s['she'] = 'her'

for i, j in s.items():
    print(i, j)

    for j in s:
        print(s[j])
        break
