# Input: Một chuỗi t (rất dài), và nhiều chuỗi s₁, s₂, ..., sₙ.
# Output: Với mỗi chuỗi sᵢ, kiểm tra xem nó có phải subsequence của t.

from collections import defaultdict
import bisect

class SubsequenceChecker:                                   # Lớp SubsequenceChecker
    def __init__(self, t: str):                             # Khởi tạo với chuỗi t
        self.char_indices = defaultdict(list)
        for i, char in enumerate(t):                        # Tạo danh sách các chỉ số cho mỗi ký tự trong t
            self.char_indices[char].append(i)               # Nếu ký tự chưa có trong char_indices, thêm nó vào

    def isSubsequence(self, s:str) -> bool:                 # Kiểm tra xem s có phải là subsequence của t hay không
        prev_index = -1                                     # Vị trí hiện tại trong t
        for char in s:                                      # Duyệt qua từng ký tự trong s
            if char not in self.char_indices:               # Nếu ký tự không có trong t, trả về False
                return False
            indices = self.char_indices[char]               # Lấy danh sách các chỉ số của ký tự trong t
            pos = bisect.bisect_right(indices, prev_index)  # Tìm chỉ số lớn nhất trong indices mà lớn hơn prev_index
            if pos == len(indices):                         # Nếu không tìm thấy chỉ số hợp lệ, trả về False
                return False           
            prev_index = indices[pos]                       # Cập nhật prev_index với chỉ số tìm được
        return True                                         # Nếu duyệt hết s mà không gặp vấn đề gì, trả về True

# Example usage
checker = SubsequenceChecker("ahbgdc")

print(checker.isSubsequence("abc"))  #  True
print(checker.isSubsequence("axc"))  #  False
print(checker.isSubsequence("gdc"))  #  True

