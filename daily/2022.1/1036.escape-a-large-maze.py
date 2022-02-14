from typing import List, Set, Tuple
from collections import deque

class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:

        def bfs(blocked: List[List[int]], source: List[int], target: List[int]):
            queue = deque()
            n = 10 ** 6
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            setBlocked = set()
            for i in blocked:
                setBlocked.add(tuple(i))

            visited = set()

            queue.append(source)
            visited.add(tuple(source))
            while queue:
                if len(queue) >= 200:
                    return True
                tempX, tempY = deque.popleft(queue)

                for deltaX, deltaY in directions:
                    nxtX = tempX + deltaX
                    nxtY = tempY + deltaY
                    nxtPoint = (nxtX, nxtY)

                    if 0 <= nxtX < n and 0 <= nxtY < n and nxtPoint not in setBlocked and nxtPoint not in visited:
                        if nxtX == target[0] and nxtY == target[1]:
                            return True
                        queue.append(nxtPoint)
                        visited.add(nxtPoint)

            return False
        return bfs(blocked, source, target) and bfs(blocked, target, source)

test = Solution()
print(test.isEscapePossible(blocked = [], source = [0,0], target = [999999,999999]))

