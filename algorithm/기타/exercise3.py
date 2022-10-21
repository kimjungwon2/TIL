import math

n = 1000

array = [True for _ in range(n+1)]




for i in range(2,int(math.sqrt(n))+1):
    if array[i] ==True: # i가 소수인 경우
        j=2
        #i의 모든 배수 지우기
        while i*j<=n:
            array[i*j] = False
            j+=1

#모든 소수 출력
for i in range(2,n+1):
    if array[i]==True:
        print(i, end=' ')
