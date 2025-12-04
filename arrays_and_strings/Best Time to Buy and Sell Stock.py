from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sort_prices = prices.copy()
        sort_prices.sort()
        
        index = prices.index(sort_prices[0])
        
        if index == len(prices) - 1:
            return 0
        
        largest = sort_prices[0]

        for i in range(index, len(prices)):
            if largest < prices[i]:
                largest = prices[i]
        return largest - sort_prices[0]

    

sol = Solution()

prices = [7, 2, 3, 4, 5, 1]

result = sol.maxProfit(prices)
print(result)
