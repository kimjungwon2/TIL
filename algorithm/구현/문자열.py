a = [3, 5, 1, 2, 2]


arr = 3561

while (True):

    for index, i in enumerate(a):
        if (index == len(a)-1):
            print(index, len(a))

        print('index:'+str(index)+', num:'+str(i))

    if (arr == 3574):
        break

    arr += 1
    a = []

    for i in str(arr):
        a.append(int(i))

    print(a)

s = [3, 5, 11, 3]
print(list(map(str, s)))


d = '32345'

for i in d:
    print(i)

print('리스트')

for i in s:
    print(i)

s = 123213

print('문자열')
for i in str(s):
    print(i)


