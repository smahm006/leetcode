class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        for char in tokens:
            match char:
                case "+":
                    one = int(stack.pop())
                    two = int(stack.pop())
                    stack.append(two + one)
                case "-":
                    one = int(stack.pop())
                    two = int(stack.pop())
                    stack.append(two - one)
                case "*":
                    one = int(stack.pop())
                    two = int(stack.pop())
                    stack.append(two * one)
                case "/":
                    one = int(stack.pop())
                    two = int(stack.pop())
                    stack.append(int(two / one))
                case _:
                    stack.append(char)
        return stack[-1]


sol = Solution()
test = ["2", "1", "+", "3", "*"]
test = ["4", "13", "5", "/", "+"]
test = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(sol.evalRPN(test))
