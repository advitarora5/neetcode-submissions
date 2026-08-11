class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            seen = defaultdict(int)
            for j in range(len(board[i])):
                current = board[i][j]
                seen[current] += 1
                if current != ".":
                    if seen[current] > 1 or (int(current) > 9 or int(current) < 1):
                        return False
        
        for i in range(len(board[0])):
            seen = defaultdict(int)
            for j in range(len(board)):
                current = board[j][i]
                seen[current] += 1
                if current != ".":
                    if seen[current] > 1 or (int(current) > 9 or int(current) < 1):
                        return False
        
        for row_start in range(0, 9, 3):
            for col_start in range (0, 9, 3):
                seen = defaultdict(int)
                for i in range(row_start, row_start + 3):
                    for j in range(col_start, col_start + 3):
                        current = board[i][j]
                        seen[current] += 1
                        if current != ".":
                            if seen[current] > 1 or (int(current) > 9 or int(current) < 1):
                                return False
        
        return True

