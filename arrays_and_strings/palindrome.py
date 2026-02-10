class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        reversed = s[::-1]
        return s == reversed
        

s = Solution()

print(s.isPalindrome(121))
