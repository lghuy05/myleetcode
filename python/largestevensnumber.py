class Solution:
    def largestEven(self, s: str) -> str:
        # convert s into intege
        n = int(s)
        while n:
            last_digit = n % 10
            if n % 2 == 0:
                return str(n)
            n //= 10
        return ""
