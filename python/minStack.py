from typing import List


class MinStack:
    def __init__(self):
        self.stack: List[int] = []
        self.minStack: List[int] = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        if self.stack:
            a: int = self.stack.pop()
            if a == self.minstack[-1] and self.minstack:
                self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.minStack[-1] if self.minStack else None
