from typing import List
class Solution:
    def sortedArray(self, my_array:List[int]) ->List[int]:
        n = len(my_array)
        for i in range(1, n):
            insert_index = i
            current_value = my_array.pop(i)
            for j in range(i - 1, -1, -1):
                if my_array[j] > current_value:
                    insert_index = j
            my_array.insert(insert_index, current_value)
        return my_array
my_array = [64, 34, 25, 12, 22, 11, 90, 5]
sol = Solution()
print(sol.sortedArray(my_array))