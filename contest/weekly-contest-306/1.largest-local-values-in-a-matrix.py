"""
题目: 矩阵中的局部最大值
链接: https://leetcode-cn.com/problems/largest-local-values-in-a-matrix/
"""

from typing import *
from collections import *
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = [[0 for _ in range(n - 2)] for _ in range(n - 2)]
        for i in range(n - 2):
            for j in range(n - 2):
                ans[i][j] = max(ans[i][j], max(grid[i][j:j + 3]))
                ans[i][j] = max(ans[i][j], max(grid[i + 1][j:j + 3]))
                ans[i][j] = max(ans[i][j], max(grid[i + 2][j:j + 3]))
        return ans

test = Solution()
print(test.largestLocal([[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]))