from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        for i in range(n - 1):
            swapped = False
            for j in range(n - i -1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swapped = True
            if not swapped:
                break

#Example:
sol = Solution()
nums1 = [2, 0, 2, 1, 1, 0]
sol.sortColors(nums1)
print(nums1)  # Output: [0, 0, 1, 1, 2, 2]

nums2 = [2, 0, 1]
sol.sortColors(nums2)
print(nums2)  # Output: [0, 1, 2]