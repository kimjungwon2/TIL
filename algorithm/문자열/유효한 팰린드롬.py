import re


def pell(str):
    a = []

    for s in str:
        if (s.isalpha()):
            a.append(s.lower())

    if (a == a[::-1]):
        return True

    return False


def isPalin(str):
    str = str.lower()
    str = re.sub('[^a-z0-9]', '', str)

    return str == str[::-1]


print(pell("A man, a plan, a canal: Panama"))
print(pell("race a car"))

print(isPalin("A man, a plan, a canal: Panama"))
print(isPalin("race a car"))
