from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # Transpose
        for i in range(n):
            for j in range(i + 1,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Reversed
        for row in matrix:
            row.reverse()

#Example:
sol = Solution()
matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
sol.rotate(matrix1)
print(matrix1)  # [[7,4,1],[8,5,2],[9,6,3]]

matrix2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
sol.rotate(matrix2)
print(matrix2) # [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]