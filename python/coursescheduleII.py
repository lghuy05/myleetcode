from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []
        hashmap = {i: [] for i in range(numCourses)}
        for i, j in prerequisites:
            hashmap[i].append(j)

        visited = set()
        alr = set()

        def dfs(node):
            if hashmap[node] == []:
                if node not in alr:
                    result.append(node)
                alr.add(node)
                return True
            if node in visited:
                return False
            visited.add(node)
            for pre in hashmap[node]:
                if not dfs(pre):
                    return False
            visited.remove(node)
            hashmap[node] = []
            if node not in alr:
                result.append(node)
            alr.add(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return result


sol = Solution()
print(sol.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
