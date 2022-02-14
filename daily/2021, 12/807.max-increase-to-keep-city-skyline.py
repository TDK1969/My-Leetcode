from typing import List

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        rowMax = [max(grid[i]) for i in range(row)]
        colMax = []
        for n in range(col):
            temp = -1
            for m in range(row):
                temp = max(temp, grid[m][n])
            colMax.append(temp)

        count = 0
        for i in range(row):
            for j in range(col):
                count += min(rowMax[i], colMax[j]) - grid[i][j]

        return count

test = Solution()
grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
print(test.maxIncreaseKeepingSkyline(grid))