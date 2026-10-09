class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS * COLS - 1

        while l <= r:
            m = (l + r) // 2
            m_row = m // COLS
            m_col = m % COLS
            cur = matrix[m_row][m_col]
            if cur > target:
                r = m - 1
            elif cur < target:
                l = m + 1
            else:
                return True
        return False
        