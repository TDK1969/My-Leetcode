from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        temp = [0]
        n = len(graph)

        def dfs(node: int):
            if node == n - 1:
                ans.append(temp.copy())
                return
            for nxt in graph[node]:
                temp.append(nxt)
                dfs(nxt)
                temp.pop()

        dfs(0)
        return ans
test = Solution()
print(test.allPathsSourceTarget([[1,2],[3],[3],[]]))
