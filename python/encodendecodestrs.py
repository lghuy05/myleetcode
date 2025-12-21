from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "`" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            # Find the delimiter
            j = i
            while s[j] != "`":
                j += 1
            # Get the length
            length = int(s[i:j])
            # Get the string
            decoded.append(s[j + 1 : j + 1 + length])
            # Move to next
            i = j + 1 + length
        return decoded
