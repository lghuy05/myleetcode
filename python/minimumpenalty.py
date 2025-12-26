class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        prefix = [0] * (n + 2)
        postfix = [0] * (n + 2)
        result = 0
        for i in range(n):
            if customers[i] == "N":
                prefix[i + 2] = prefix[i + 1] + 1
            else:
                prefix[i + 2] = prefix[i + 1]

        for i in range(n - 1, -1, -1):
            if customers[i] == "Y":
                postfix[i + 1] = postfix[i + 2] + 1
            else:
                postfix[i + 1] = postfix[i + 2]

        min_pel = float("inf")
        day = 0
        for pre, pos in zip(prefix[1:], postfix[1:]):
            if min_pel > pre + pos:
                min_pel = pre + pos
                result = day
            day += 1

        return result


sol = Solution()
print(sol.bestClosingTime("YYNY"))
print(sol.bestClosingTime("YYYY"))
