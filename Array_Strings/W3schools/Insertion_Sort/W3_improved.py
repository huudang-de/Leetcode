from typing import List
class Solution:
    def importSortedArray(self, my_array:List[int]) -> List[int]:
        n = len(my_array)
        for i in range(1, n):
            insert_index = i
            current_value = my_array[i]
            for j in range(i - 1, -1 , -1):
                if my_array[j] > current_value:
                    my_array[j + 1] = my_array[j]
                    insert_index = j
                else:
                    break
            my_array[insert_index] = current_value
        return my_array
my_array = [64, 34, 25, 12, 22, 11, 90, 5]
sol = Solution()
print(sol.importSortedArray(my_array))