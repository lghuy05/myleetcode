from typing import List


class Solution:
    def validateCoupons(
        self, code: List[str], businessLine: List[str], isActive: List[bool]
    ) -> List[str]:
        result = []
        category = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}
        ordered_cat = {cat: [] for cat in category.values()}
        n = len(code)
        for i in range(n):
            if not isActive[i] or not code[i] or businessLine[i] not in category:
                continue
            flag = False
            for j in code[i]:
                if not j.isalnum() and j != "_":
                    flag = True
                    break
            if flag:
                continue
            ordered_cat[category[businessLine[i]]].append(code[i])

        for i in ordered_cat:
            ordered_cat[i].sort()

        for i in ordered_cat:
            result.extend(ordered_cat[i])
        return result


sol = Solution()
print(
    sol.validateCoupons(
        ["SAVE20", "", "PHARMA5", "SAVE@20"],
        ["restaurant", "grocery", "pharmacy", "restaurant"],
        [True, True, True, True],
    )
)
print(
    sol.validateCoupons(
        ["GROCERY15", "ELECTRONICS_50", "DISCOUNT10"],
        ["grocery", "electronics", "invalid"],
        [False, True, True],
    )
)
