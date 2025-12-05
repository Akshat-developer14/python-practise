from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False
    
sol = Solution()

nums = [7, 1, 3, 3, 6, 4]

result = sol.containsDuplicate(nums)
print(result)
