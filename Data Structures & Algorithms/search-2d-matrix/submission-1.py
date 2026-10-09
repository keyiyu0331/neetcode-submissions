class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l <= r:
            mid_r = (l + r) // 2
            if target >= matrix[mid_r][0] and target <= matrix[mid_r][-1]:
                r = matrix[mid_r]
                i, j = 0, len(r) - 1
                while i <= j:
                    mid = (i + j) // 2
                    if r[mid] == target:
                        return True
                    elif r[mid] < target:
                        i = mid + 1
                    else:
                        j = mid - 1
                return False
            elif target > matrix[mid_r][-1]:
                l = mid_r + 1
            elif target < matrix[mid_r][0]:
                r = mid_r - 1
        return False
        