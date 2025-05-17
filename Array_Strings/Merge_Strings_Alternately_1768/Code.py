class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []                             # Initialize an empty list to store the merged characters(Khởi tạo một danh sách rỗng để lưu trữ các ký tự đã hợp nhất)
        max_len = max(len(word1), len(word2))   # Find the maximum length of the two strings (Tìm chiều dài tối đa của hai chuỗi)
        
        for i in range(max_len):                # Loop through the range of the maximum length (Tiến hành lặp qua khoảng cách của chiều dài tối đa)
            if i < len(word1):                  # If the index is within the bounds of word1 (Nếu chỉ số nằm trong giới hạn của word1)
                result.append(word1[i])         # Append the character from word1 to the result (Thêm ký tự từ word1 vào kết quả)
            if i < len(word2):                  # If the index is within the bounds of word2 (Nếu chỉ số nằm trong giới hạn của word2)
                result.append(word2[i])         # Append the character from word2 to the result (Thêm ký tự từ word2 vào kết quả)
        return ''.join(result)                  # Join the list of characters into a single string and return it (Kết hợp danh sách các ký tự thành một chuỗi duy nhất và trả về nó)

# Example usage:
solution = Solution()                           # Create an instance of the Solution class (Tạo một thể hiện của lớp Solution)
print(solution.mergeAlternately("abc", "pqr"))  # Output: "apbqcr"
print(solution.mergeAlternately("ab", "pqrs"))  # Output: "apbqrs"
print(solution.mergeAlternately("abcd", "pq"))  # Output: "apbqcd"


