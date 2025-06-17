from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            min_index = i
            for j in range( i + 1, n):
                if nums[j] < nums[min_index]:
                    min_index = j
            nums[i], nums[min_index] = nums[min_index], nums[i]
        return nums

nums = [2, 3,56, 1, 66, 23, 11]
sol = Solution()
print(sol.sortArray(nums))