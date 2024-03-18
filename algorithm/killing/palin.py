class Solution(object):
    def partition(self, s):
        answer = []

        def is_palindrome(a):
            return a == a[::-1]

        def back(start, path):
            if start == len(s):
                answer.append(path[:])
                return

            for i in range(start + 1, len(s) + 1):
                if is_palindrome(s[start:i]):
                    path.append(s[start:i])
                    back(i, path)
                    path.pop()

        back(0, [])

        return answer

solution = Solution()
s = "aab"
result = solution.partition(s)
print(result)