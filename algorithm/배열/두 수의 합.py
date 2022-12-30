def twoSum(lis, target):
    result = []
    length = len(lis)

    for i in range(length):
        for j in range(i+1, length):
            if (target == lis[i]+lis[j]):
                result.append(i)
                result.append(j)
                break

    return result


print(twoSum([2, 7, 11, 15], 9))
