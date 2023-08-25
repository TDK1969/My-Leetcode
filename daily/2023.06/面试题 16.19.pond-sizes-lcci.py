"""
日期: 2023-06-22
题目: 水域大小
链接: https://leetcode-cn.com/problems/pond-sizes-lcci/
"""

from typing import *
from collections import *
class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        m, n = len(land), len(land[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        ans = []
        directions = [[-1, -1], [-1, 0], [-1, 1],[0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

        for i in range(m):
            for j in range(n):
                if visited[i][j] == 0 and land[i][j] == 0:
                    q = deque()
                    q.append((i, j))
                    visited[i][j] = 1
                    cnt = 1

                    while q:
                        temp_x, temp_y = q.popleft()
                        for dx, dy in directions:
                            next_x, next_y = temp_x + dx, temp_y + dy
                            if 0 <= next_x < m and 0 <= next_y < n and \
                                visited[next_x][next_y] == 0 and \
                                land[next_x][next_y] == 0:
                                cnt += 1
                                q.append((next_x, next_y))
                                visited[next_x][next_y] = 1
                    if cnt != 0:
                        ans.append(cnt)
        
        ans.sort()
        return ans
    
test = Solution()
print(test.pondSizes([
  [0,2,1,0],
  [0,1,0,1],
  [1,1,0,1],
  [0,1,0,1]
]))



        