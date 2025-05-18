class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000
        }

        total = 0                                           # Tổng = 0
        prev_value = 0                                      # Giá trị trước đó = 0

        for char in reversed(s):                            # Duyệt từng ký tự trong chuỗi từ cuối lên đầu
            current_value = roman[char]                     # Giá trị hiện tại = giá trị của ký tự hiện tại
            if current_value < prev_value:                  # Nếu giá trị hiện tại nhỏ hơn giá trị trước đó
                total -= current_value                      # Trừ giá trị hiện tại khỏi tổng
            else:
                total += current_value                      # Cộng giá trị hiện tại vào tổng
            prev_value = current_value                      # Cập nhật giá trị trước đó
        return total                                        # Trả về tổng giá trị

# Example usage
col = Solution()
print(col.romanToInt("MCMXCIV"))                            # Kết quả: 1994