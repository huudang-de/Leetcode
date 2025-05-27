from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x:x[0])                          #Sắp xếp theo điểm bắt đầu
        merged = []                                                 #Tạo danh sách chứa kết quả

        for interval in intervals:                                  #Duyệt từng khoảng
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)                             #Nếu không chồng lấn -> thêm mới
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])     #Nếu chồng -> gộp
        return merged                                               #Trả về danh sách đã gộp

#Example:
sol = Solution()
print(sol.merge([[1,3],[2,6],[8,10],[15,18]])) #[[1,6],[8,10],[15,18]]
print(sol.merge([[1,4],[4,5]])) #[[1,5]]