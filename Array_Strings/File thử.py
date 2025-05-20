'''Cách làm: cho điểm gốc = 0, duyệt từng word , nếu i nhỏ maxlen(word) thì thêm vào danh sách'''

class Solution:
    def mergedStrings(self, word1:str, word2:str) -> str:
        result = []
        max_len = max(len(word1), len(word2))

        for i in range(max_len):
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])
        return ''.join(result)

# Example usage
col = Solution()
print(col.mergedStrings("abc", "pqr"))  # Kết quả: "apbqcr"


