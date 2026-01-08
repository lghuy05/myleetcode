from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right = 0, 0
        arr_t = [0] * 128
        checked, required = 0, 0
        arr_s = [0] * 128
        min_len = float("inf")
        min_left = 0
        n = len(s)
        for i in t:
            arr_t[ord(i)] += 1
        # for i in arr_t:
        #     if i > 0:
        #         required += 1
        required = len(t)
        while right < n:
            arr_s[ord(s[right])] += 1
            # if arr_s[ord(s[right])] == arr_t[ord(s[right])]:
            #     checked += 1
            if arr_s[ord(s[right])] <= arr_t[ord(s[right])]:
                checked += 1
            while left <= right and checked == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_left = left
                arr_s[ord(s[left])] -= 1
                if arr_s[ord(s[left])] < arr_t[ord(s[left])]:
                    checked -= 1
                left += 1
            right += 1
        return "" if min_len == float("inf") else s[min_left : min_left + min_len]


sol = Solution()
print(sol.minWindow("aa", "aa"))
print(sol.minWindow("OUZODYXAZV", "XYZ"))
