from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        ans = []

        for i in range(n):
            locate = i
            for j in range(m):
                if grid[j][locate] == 1 and locate == n - 1 or grid[j][locate] == 1 and grid[j][locate + 1] == -1:
                    ans.append(-1)
                    break
                elif grid[j][locate] == -1 and locate == 0 or grid[j][locate] == -1 and grid[j][locate - 1] == 1:
                    ans.append(-1)
                    break
                else:
                    if grid[j][locate] == 1:
                        locate += 1
                    else:
                        locate -= 1
            if len(ans) != i + 1:
                ans.append(locate)

        return ans

test = Solution()
print(test.findBall([[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]))