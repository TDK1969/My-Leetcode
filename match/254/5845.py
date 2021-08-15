from typing import List
from collections import deque


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        l = 0
        r = len(cells) - 1
        dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while l <= r:
            mid = (l + r) // 2
            matrix = [[0 for _ in range(col)] for _ in range(row)]
            for i in range(mid):
                matrix[cells[i][0] - 1][cells[i][1] - 1] = 1
            visited = set()
            flag = False
            queue = deque()
            for i in range(col):
                queue.append((0, i))
                visited.add((0, i))

            while queue and not flag:
                x, y = queue.popleft()
                if x < 0 or y < 0 or y >= col or matrix[x][y] == 1:
                    continue
                if x == row - 1:
                    flag = True
                for dx, dy in dir:
                    if (x + dx, y + dy) not in visited:
                        queue.append((x + dx, y + dy))
                        visited.add((x + dx, y + dy))
            if flag:
                l = mid + 1
            else:
                r = mid - 1
        return r

test = Solution()
print(test.latestDayToCross(3, 3, [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]))



