class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if not s:
            return False
        for char in s:
            if char in ["(", "{", "["]:
                stack.append(char)
            else:
                if len(stack) == 0 or stack.pop() + char not in ["()", "[]", "{}"]:
                    return False
        if len(stack) != 0:
            return False
        return True


sol = Solution()
# test = "({[]})"
# test = "()[]{}"
# test = "(){[]}"
# test = "(]"
# test = "("
# test = ")"
print(sol.isValid(test))
