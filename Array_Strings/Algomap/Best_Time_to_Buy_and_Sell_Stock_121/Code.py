from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
                
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit
        return max_profit
# Example usage:
col = Solution()
print(col.maxProfit([7, 1, 5, 3, 6, 4]))  # Output: 5
print(col.maxProfit([7, 6, 4, 3, 1]))  # Output: 0