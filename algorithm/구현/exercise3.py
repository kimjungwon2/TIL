a = input()
x = int(ord(a[0]))-int(ord('a')) + 1
y = int(a[1])


moves = [(-2, -1), (-1, -2), (1, -2), (2, -1),
         (2, 1), (1, 2), (-1, 2), (-2, 1)]

count = 0

for move in moves:
    nx = x+move[0]
    ny = y + move[1]

    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue

    count+=1


print(count)
