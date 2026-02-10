from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]
        # output = [1, 1, 2, 3]

        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix # [1, 32, 8, 3]
            suffix *= nums[i] # 4, 32,  
        # output = [1, 1, 2, 3]

        return output

sol = Solution()

list1 = [1, 2, 3, 4]
# result -> [24, 12, 8, 6]
result = sol.productExceptSelf(list1)

print(result)
