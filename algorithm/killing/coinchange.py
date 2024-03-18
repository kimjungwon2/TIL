from collections import deque

class Solution:
    def coinChange(self, coins, amount):
        visited = [False] * (amount+1)
        
        def bfs(sum):
            queue = deque([(sum, 0)])

            while queue:
                amt, n = queue.popleft()

                if amt == 0:
                    return n

                for c in coins:
                    next_c = amt - c

                    if next_c >= 0 and not visited[next_c]:
                        queue.append((next_c, n+1))
                        visited[next_c] = True
            
            return -1

        return bfs(amount)

# 입력 값 설정
coins = [1, 2, 5]
amount = 11

# Solution 클래스 인스턴스 생성
solution = Solution()

# 결과 출력
print(solution.coinChange(coins, amount))