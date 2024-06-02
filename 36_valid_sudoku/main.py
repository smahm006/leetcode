class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        lenb = len(board)
        squ_digits = [{str(i): 0 for i in range(1, lenb + 1)} for _ in range(9)]
        for i in range(len(board)):
            row_digits = {str(i) : 0 for i in range(1, lenb+1)}
            col_digits = {str(i) : 0 for i in range(1, lenb+1)}
            for j in range(len(board)):
                if board[i][j] != ".":
                    row_digits[board[i][j]] += 1
                    if (i >= 0 and i <= 2) and (j >= 0 and j <= 2):
                        squ_digits[1][board[i][j]] += 1
                    if (i >= 0 and i <= 2) and (j >= 3 and j <= 5):
                        squ_digits[2][board[i][j]] += 1
                    if (i >= 0 and i <= 2) and (j >= 6 and j <= 8):
                        squ_digits[3][board[i][j]] += 1
                    if (i >= 3 and i <= 5) and (j >= 0 and j <= 2):
                        squ_digits[4][board[i][j]] += 1
                    if (i >= 3 and i <= 5) and (j >= 3 and j <= 5):
                        squ_digits[5][board[i][j]] += 1
                    if (i >= 3 and i <= 5) and (j >= 6 and j <= 8):
                        squ_digits[6][board[i][j]] += 1
                    if (i >= 6 and i <= 8) and (j >= 0 and j <= 2):
                        squ_digits[7][board[i][j]] += 1
                    if (i >= 6 and i <= 8) and (j >= 3 and j <= 5):
                        squ_digits[8][board[i][j]] += 1
                    if (i >= 6 and i <= 8) and (j >= 6 and j <= 8):
                        squ_digits[0][board[i][j]] += 1
                if board[j][i] != ".":
                    col_digits[board[j][i]] += 1
            if any(x > 1 for x in row_digits.values()) or any(x > 1 for x in col_digits.values()):
                return False
        for square in squ_digits:
            if any(x > 1 for x in square.values()):
                return False
        return True

sol = Solution()
test = [[".",".",".",".","5",".",".","1","."],
        [".","4",".","3",".",".",".",".","."],
        [".",".",".",".",".","3",".",".","1"],
        ["8",".",".",".",".",".",".","2","."],
        [".",".","2",".","7",".",".",".","."],
        [".","1","5",".",".",".",".",".","."],
        [".",".",".",".",".","2",".",".","."],
        [".","2",".","9",".",".",".",".","."],
        [".",".","4",".",".",".",".",".","."]]
print(sol.isValidSudoku(test))
