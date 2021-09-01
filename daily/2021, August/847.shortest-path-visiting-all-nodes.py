from typing import List


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        queue = [(i, 1 << i) for i in range(n)]
        visited = set(queue)
        goal = 2 ** n - 1
        step = 0

        while queue:
            next = []
            for node, state in queue:
                if state == goal:
                    return step
                for next_node in graph[node]:
                    if (next_node, state | 1 << next_node) not in visited:
                        next.append((next_node, state | 1 << next_node))
                        visited.add((next_node, state | 1 << next_node))
            queue = next
            step += 1
        return -1
test = Solution()
print(test.shortestPathLength([[1,2,3],[0],[0],[0]]))