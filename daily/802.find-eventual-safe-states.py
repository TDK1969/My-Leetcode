from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        color = [0] * n

        def safe(x: int) -> bool:
            if color[x] != 0:
                return color[x] == 2
            color[x] = 1
            for next_node in graph[x]:
                if not safe(next_node):
                    return False
            color[x] = 2
            return True

        return [i for i in range(n) if safe(i)]

test = Solution()
print(test.eventualSafeNodes([[0],[2,3,4],[3,4],[0,4],[]]))

