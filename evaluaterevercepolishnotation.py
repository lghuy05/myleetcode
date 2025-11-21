from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            if s == "+":
                a = stack.pop()
                stack[-1] += int(a)
            elif s == "-":
                a = stack.pop()
                stack[-1] -= int(a)
            elif s == "*":
                a = stack.pop()
                stack[-1] *= int(a)
            elif s == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(a / b))
            else:
                stack.append(int(s))

        return stack[0]
