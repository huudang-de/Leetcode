from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        s = len(nums)
        output = [1] * s

        left = 1
        for i in range(s):
            output[i] = left
            left *= nums[i]

        right = 1
        for i in reversed(range(s)):
            output[i] *= right
            right *= nums[i]

        return output

if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    nums1 = [1, 2, 3, 4]
    print("Input:", nums1)
    print("Output:", sol.productExceptSelf(nums1))

    # Test case 2
    nums2 = [-1, 1, 0, -3, 3]
    print("Input:", nums2)
    print("Output:", sol.productExceptSelf(nums2))


