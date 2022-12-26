def pell(str):
    a = []

    for s in str:
        if (s.isalpha()):
            a.append(s.lower())

    if (a == a[::-1]):
        return True

    return False


print(pell("A man, a plan, a canal: Panama"))
print(pell("race a car"))
