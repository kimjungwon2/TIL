from collections import Counter


def topKFrequent(nums, k):
    return list(zip(*Counter(nums).most_common(k)))[0]


print(topKFrequent([1, 1, 1, 2, 2, 3], 2))
