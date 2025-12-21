from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # count = 0
        # columns = len(strs[0])
        # rows = len(strs)
        # for i in range(columns):
        #     li = [0] * 26
        #     last = -1
        #     for j in range(rows):
        #         if ord(strs[j][i]) < last:
        #             count += 1
        #             break
        #         li[ord(strs[j][i]) - ord("a")] += 1
        #         last = max(last, ord(strs[j][i]))
        # return count
        #
        count = 0
        columns = len(strs[0])
        rows = len(strs)
        for i in range(columns):
            last = "a"
            for j in range(rows):
                if strs[j][i] < last:
                    count += 1
                    break
                last = strs[j][i]
        return count


sol = Solution()
print(sol.minDeletionSize(["cba", "daf", "ghi"]))
