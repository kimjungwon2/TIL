from collections import Counter


def count(s1, s2):
    freqs = Counter(s1)
    count = 0

    for char in s2:
        count += freqs[char]

    return count


print(count("aA", "aAAbbbb"))
