def is_prime(x):

    for i in range(2,x):
        if x%i ==0:
            return False

    return True

print(is_prime(4))
print(is_prime(14))
print(is_prime(17))
