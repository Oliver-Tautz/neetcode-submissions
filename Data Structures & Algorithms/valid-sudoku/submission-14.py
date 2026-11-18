from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                print(f"{i},{j}: {board[i][j]}")
                print(rows,cols,squares)
                if board[i][j] == '.': continue
                # Rows
                if board[i][j] in rows[i]:
                    return False
                else:
                    rows[i].add(board[i][j])

                # Cols
                if board[i][j] in cols[j]:
                    return False
                else:
                    cols[j].add(board[i][j])
                
                # squares
                if board[i][j] in squares[str(i//3)+str(j//3)]:
                    return False
                else:
                    squares[str(i//3)+str(j//3)].add(board[i][j])

        return True
                
