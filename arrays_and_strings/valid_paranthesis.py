class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i == '(' or '[' or '{':
                stack.append(i)
            else:
                if stack.pop() == '(' and i == ')':
                    pass
                if stack.pop() == '[' and i == ']':
                    pass
                if stack.pop() == '{' and i == '}':
                    pass
                else:
                    stack.append(i)
        if len(stack) > 0:
            return False
        else:
            return True

s = Solution()

print(s.isValid('([])'))