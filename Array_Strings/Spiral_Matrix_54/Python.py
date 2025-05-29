from typing import List
class Colution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        if not matrix:
            return result
        
        top, bottom = 0, len(matrix)- 1
        left, right = 0, len(matrix[0])- 1

        while top <= bottom and left <= right:
            # Đi sang phải
            for col in range(left, right+ 1):
                result.append(matrix[top][col])
            top += 1

            # Đi sang trái
            for row in range(top, bottom+ 1):
                result.append(matrix[row][right])
            right -= 1

            # Đi sang trái
            if top <= bottom:
                for col in range(right, left -1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1
            
            # Đi lên
            if left <= right:
                for row in range(bottom, top -1, -1):
                    result.append(matrix[row][left])
                left += 1
        
        return result
    
#Example
sol = Colution()
print(sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))