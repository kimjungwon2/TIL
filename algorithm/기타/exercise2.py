import math
from operator import truediv

def is_prime(x):
    for i in range(2,int(x**0.5)+1):
        # x가 해당 수로 나누어 떨어지면 소수가 아니다.
        if x%i==0:
            return False
    return True


print(is_prime(4))
print(is_prime(14))
print(is_prime(17))
