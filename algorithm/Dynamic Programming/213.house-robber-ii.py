from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums) - 1
        # 环的动态规划，将环拆成两个队列，一个从0~n-1，一个从1到n
        dp1 = [0 for _ in range(n)]
        dp2 = [0 for _ in range(n)]
        dp1[0] = nums[0]
        dp2[0] = nums[1]
        for i in range(1, n):
            dp1[i] = max(dp1[i - 1], nums[i] + dp1[i - 2])
        for j in range(2, n + 1):
            dp2[j - 1] = max(dp2[j - 2], dp2[j - 3] + nums[j])
        return max(dp1[-1], dp2[-1])

test = Solution()
print(test.rob([2,3,2]))