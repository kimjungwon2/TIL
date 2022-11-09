def isPrime(x):
    for i in range(2, int(x**0.5)+1):
        if (x % 2 == 0):
            return False

    return True


print(isPrime(4))
print(isPrime(5))
