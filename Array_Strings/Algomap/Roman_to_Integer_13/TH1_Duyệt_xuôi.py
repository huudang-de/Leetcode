class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000
        }

        total = 0                                           # Tổng = 0
        n = len(s)                                          # Độ dài của chuỗi

        for i in range(n):                                  # Duyệt từng ký tự trong chuỗi
            if i < n - 1 and roman[s[i]] < roman[s[i+1]]:   # Nếu ký tự hiện tại nhỏ hơn ký tự tiếp theo
                total -= roman[s[i]]                        # Trừ giá trị của ký tự hiện tại
            else:
                total += roman[s[i]]                        # Cộng thêm giá trị của ký tự hiện tại
        return total                                        # Trả về tổng giá trị

# Example usage
col = Solution()
print(col.romanToInt("MCMXCIV"))
