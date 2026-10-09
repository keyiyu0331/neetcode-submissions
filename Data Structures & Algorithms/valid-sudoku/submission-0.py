class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.isRowValid(board) and self.isColValid(board) and self.isSubBoxValid(board)

    def isRowValid(self, board):
        for row in board:
            num = [i for i in row if i != "."]
            if len(set(num)) != len(num):
                return False
        return True

    def isColValid(self, board):
        for i in range(9):
            col = []
            for j in range(9):
                if board[j][i] != ".":
                    col.append(board[j][i])
            if len(set(col)) != len(col):
                return False
        return True
   
    def isSubBoxValid(self, board):
        for box_row in range(0, 9, 3): #row
            for box_col in range(0, 9, 3): #col
                box = []
                for r in range(3):
                    for c in range(3):
                        if board[box_row + r][box_col + c] != ".":
                            box.append(board[box_row + r][box_col + c])
                if len(set(box)) != len(box):
                    return False
        return True
