class Solution(object):
    def solveNQueens(self, n):
        result = []
        
        def check(row, col):
            for i in range(row):
                if board[i] == col or abs(board[i] - col) == row - i:
                    return False
            return True

        def back(result, row):
            if row == n:
                temp_result = []
                for i in board:
                    row = ''
                    for col in range(n):
                        if col == i:
                            row += 'Q'
                        else:
                            row += '.'
                    temp_result.append(row)
                result.append(temp_result)
                return
                
            for col in range(n):
                if check(row, col):
                    board[row] = col
                    back(result, row + 1)

        for i in range(n):
            board = [-1] * n
            board[0] = i
            back(result, 1)

        return result

solution = Solution()
n = 4
result = solution.solveNQueens(n)
for board in result:
    for row in board:
        print(row)