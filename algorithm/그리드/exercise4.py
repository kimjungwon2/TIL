n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 #그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수 

for i in data: #공포도 낮은 것부터 하나씩 확인 
    count +=1 #그룹에 모험가 포함시키기
    if count>=i: #모험가 수가 현재의 공포도 이상이면, 그룹 결성
        result +=1 #그룹의 수 증가시키기
        count = 0 #그룹에 포함된 모험가 수 초기화

print(result)    

