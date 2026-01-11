from typing import List
from collections import deque

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ''' 
    pseudo code
    func main(s):
        result = []
        backtrack(0, [])
        return result

    func backtrack(start, currentPartition):
        if start is equal to len of string:
            add currentPartition copy to result
        for end from start to length of s:
            substring = s from start to end
            if substring is a palindrome:
                add substring to currentPartition
                backtrack(start + 1, currentPartition)
                remove the last element from currentPartition
    '''
        # recursion approach
        # result = []
        # n = len(s)
        # def backtrack(start, currentPartition):
        #     if start == n:
        #         result.append(currentPartition[:])
        #         return
        #     for end in range(start, n):
        #         substring = s[start:end+1]
        #         if substring == substring[::-1]:
        #             currentPartition.append(substring)
        #             backtrack(end + 1, currentPartition)
        #             currentPartition.pop()
        #
        # backtrack(0, [])
        # return result

        #bfs approach
        result = []
        q = deque()
        q.append((0,[]))
        n = len(s)

        while q:
            start, path = q.popleft()
            if start == n:
                result.append(path)
                continue
            for end in range(start, n):
                substring = s[start:end+1]
                if substring == substring[::-1]:
                    # path.append(substring)
                    # q.append((end+1,path))
                    q.append((end+1,path + [substring]))
                    # path.pop()
        return result
