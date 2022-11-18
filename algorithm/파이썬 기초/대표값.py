import sys
from collections import Counter
input = sys.stdin.readline

arr = [ int(input()) for _ in range(10)]
s = Counter(arr).most_common()


print(sum(arr)//10)
print(s[0][0])