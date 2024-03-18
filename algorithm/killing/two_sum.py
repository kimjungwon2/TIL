class Solution(object):
    def twoSum(self, nums, target):
        dict_num = {}
        answer = []

        for i, num in enumerate(nums):
            complement = target - num
            if complement in dict_num and dict_num[complement] != i:
                answer.append(dict_num[complement])
                answer.append(i)
                break  # 각 요소는 한 번만 사용
            dict_num[num] = i

        return answer

nums = [3, 2, 4]
target = 6
solution = Solution()
result = solution.twoSum(nums, target)
print(result)