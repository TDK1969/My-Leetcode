"""
日期: 2022-04-27
题目: 太平洋大西洋水流问题
链接: https://leetcode-cn.com/problems/pacific-atlantic-water-flow/
"""
from typing import List, Tuple
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        def bfs(start: List[Tuple[int]]):
            visited = set(start)
            queue = deque(start)
            
            while queue:
                x, y = queue.popleft()
                for nx, ny in [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]:
                    if 0 <= nx < m and 0 <= ny < n and heights[nx][ny] >= heights[x][y] and (nx, ny) not in visited:
                        queue.append((nx, ny))
                        visited.add((nx, ny))
            return visited

        pacific = [(0, i) for i in range(n)] + [(i, 0) for i in range(1, m)]
        atlantic = [(m - 1, i) for i in range(n)] + [(i, n - 1) for i in range(m - 1)]
        both = bfs(pacific) & bfs(atlantic)
        ans = [list(i) for i in both]
        return ans

test = Solution()
print(test.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))





