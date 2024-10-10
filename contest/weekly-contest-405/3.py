from typing import *
from collections import *
class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        s = [[[0, 0] for _ in range(1 + len(grid[0]))] for _ in range(1 + len(grid))]
        ans = 0
        
        for i, row in enumerate(grid, 1):
            for j, x in enumerate(row, 1):
                s[i][j][0] = (
                    s[i - 1][j][0] + s[i][j - 1][0] - s[i - 1][j - 1][0]
                )
                s[i][j][1] = (
                    s[i - 1][j][1] + s[i][j - 1][1] - s[i - 1][j - 1][1]
                )
                if x == "X" or x == "Y":
                    s[i][j][ord(x) - 88] += 1
                if s[i][j][0] == s[i][j][1]:
                    ans += 1
        return ans

                
print(Solution().numberOfSubmatrices([["X","Y","."],["Y",".","."]]))