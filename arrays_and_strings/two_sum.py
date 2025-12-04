'''
💡 The Problem Statement:-

The goal is to find two numbers in a given array of integers that add up to a specific target integer.

Input:
    1. An array of integers, nums.
    2. An integer target.

Output:
    • The indices of the two numbers in the nums array that sum up to target.

Constraints:
    • You may assume that each input would have exactly one solution.
    • You may not use the same element twice (meaning the two indices must be different).
    • The order in which you return the indices doesn't matter.
'''

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in num_map:
                return [num_map[complement], i]
            
            num_map[num] = i

        return []


sol = Solution()

nums = [2, 4, 8 , 11, 7 , 15]
target = 9

result = sol.twoSum(nums, target)

print(f"Input: {nums}, Target: {target}")
print(f"Output Indices: {result}")
