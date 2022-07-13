from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = []
        dp.append(triangle[0][0])

        for i in range(1, n):
            temp = []
            temp.append(dp[0] + triangle[i][0])
            for j in range(1, i):
                temp.append(min(dp[j - 1], dp[j]) + triangle[i][j])
            temp.append(dp[-1] + triangle[i][-1])
            dp = temp
        return min(dp)

test = Solution()
print(test.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))