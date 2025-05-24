from typing import List
class Solution:
    def summaryRanges(self, nums: List[int])->List[str]:
        result = []
        if not nums:
            return result
        
        start = 0
        for i in range(len(nums)):
            if i == len(nums) - 1 or  nums[i]+1 != nums[i+1]:
                if start == i:
                    result.append(str(nums[start]))
                else:
                    result.append(f"{nums[start]} -> {nums[i]}")
                start = i + 1
        return result

#Example
sol = Solution()
print(sol.summaryRanges([0,1,2,5,7,8]))
print(sol.summaryRanges([2,3,5,10,11,12,15]))