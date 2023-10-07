import time 

x=0

start_time =time.time()
for _ in range(1,1000):
     x+=1

print(x)

end_time = time.time()

print("time:",end_time-start_time)