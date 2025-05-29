from typing import List
class Colution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        while matrix:
            # Pop hàng đầu tiên
            result += matrix.pop(0)
            # Lấy phần tử cuối mỗi dòng còn lại (trên xuống dưới)
            if matrix and matrix[0]:
                for row in matrix:
                    result.append(row.pop())
            # Pop hàng cuối cùng (phải sang trái)
            if matrix:
                result += matrix.pop()[::-1]
            # Lấy phần tử đầu tiên mỗi hàng còn lại (dưới lên trên)
            if matrix and matrix[0]:
                for row in reversed(matrix):
                    result.append(row.pop(0))
        return result

#Example:
sol = Colution()
print(sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))