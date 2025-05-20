'''
Mục tiêu:
Kiểm tra xem khách hàng có thực hiện chuỗi hành vi đáng ngờ:
"withdraw" → "transfer" → "deposit"
trong log giao dịch dài hay không.
'''
# Mã giả log giao dịch:
log = ["login", "withdraw", "transfer", "deposit", "logout", "payment"]
pattern = ["withdraw", "transfer", "deposit"]
# Tạo một lớp để kiểm tra subsequence
class Subsequence:
    def is_subsequence(self, pattern, log):
        i = 0 
        for event in log:
            if i < len(pattern) and event == pattern[i]:
                i += 1
        return i == len(pattern)
    
# Kiểm tra xem chuỗi hành vi có phải là subsequence của log hay không
col = Subsequence()
print("⚠️ Rửa tiền:", col.is_subsequence(pattern, log))
            