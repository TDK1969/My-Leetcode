from typing import List


class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        escape = abs(target[0]) + abs(target[1])
        stop = float("inf")
        for x_ghost, y_ghost in ghosts:
            stop = min(stop, abs(x_ghost - target[0]) + abs(y_ghost - target[1]))
        return escape < stop

test = Solution()
print(test.escapeGhosts([[5,0],[-10,-2],[0,-5],[-2,-2],[-7,1]], [7,7]))
