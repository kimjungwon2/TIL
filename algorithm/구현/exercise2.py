h= int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) +str(j)+str(k): # 매 시간마다 '3'이 있으면 증가
                count+=1

print(count)