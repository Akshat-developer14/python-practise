from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            profit = price - min_price

            if profit > max_profit:
                max_profit = profit

            if price < min_price:
                min_price = price
            
        return max_profit



sol = Solution()

prices = [7, 1, 5, 3, 6, 4]

result = sol.maxProfit(prices)
print(result)
