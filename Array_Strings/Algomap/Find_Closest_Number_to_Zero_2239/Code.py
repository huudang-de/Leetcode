from typing import List

class Solution:
    def findClosestNumber(self, nums: List[int])-> int:
        closest = nums[0]                                   # Initialize closest to the first element(Khởi tạo gần nhất với phần tử đầu tiên)
        
        for num in nums:                                    # Iterate through the list to find the closest number (Lặp lại danh sách để tìm số gần nhất)
            if abs(num) < abs(closest):                     # If the absolute value of num is less than that of closest (Nếu giá trị tuyệt đối của num nhỏ hơn giá trị gần nhất)
                closest = num                               # Update closest to num(Cập nhật gần nhất với num)
            elif abs(num) == abs(closest) and num > closest:# If the absolute value of num is equal to that of closest and num is greater than closest(Nếu giá trị tuyệt đối của num bằng giá trị gần nhất và num lớn hơn gần nhất)
                closest = num
        return closest                                      # Return the closest number (Trả về số gần nhất)
    
#Example usage
nums = [-4, -2, 1, 4, 8]                                    # Có thể thử kiểu khác: nums = [2,-1,1]
sol = Solution()                                            # Tạo một đối tượng của lớp Solution)
result = sol.findClosestNumber(nums)                        #(Gọi hàm)
print(result)                                               # Output: 1