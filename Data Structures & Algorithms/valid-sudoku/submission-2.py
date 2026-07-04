class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_seen = collections.defaultdict(set)
        col_seen = collections.defaultdict(set)
        matrix_seen = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    if (board[r][c] in row_seen[r] or
                        board[r][c] in col_seen[c] or 
                        board[r][c] in matrix_seen[(r // 3, c // 3)]):
                        return False
                    row_seen[r].add(board[r][c])
                    col_seen[c].add(board[r][c])
                    matrix_seen[(r // 3, c // 3)].add(board[r][c])
        return True