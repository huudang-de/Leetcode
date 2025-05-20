class Solution:
    def isSubsequence(self, s:str, t:str) -> bool:
        i = 0
        for char in t:
            if i < len(s) and s[i] == char:
                i += 1
        return i == len(s)

# Example usage:
col = Solution()
print(col.isSubsequence("abc", "ahbgdc"))  # Output: True
print(col.isSubsequence("axc", "ahbgdc"))  # Output: False