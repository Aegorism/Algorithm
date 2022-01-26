class Solution:
    # pointer, similar to binary search: O(m + n)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = 0, len(matrix[0]) - 1
        
        while 0 <= i < len(matrix) and 0 <= j < len(matrix[0]):
            if matrix[i][j] < target:
                i += 1
            elif matrix[i][j] > target:
                j -= 1
            else:
                return True
        
        return False

    # any, in: O(mn)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return any(target in row for row in matrix)
    
     # binary search: O(mlogn)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix: # O(m)
            i = bisect.bisect_left(row, target) # O(logn)
            if i < len(row) and row[i] == target:
                return True
        
        return False