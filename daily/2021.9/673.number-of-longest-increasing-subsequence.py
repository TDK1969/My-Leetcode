from typing import List


class Solution:
    def findNumber0fLIS(self, nums: List[int]) -> int:
        n, max_len, ans = len(nums), 0, 0
        dp = [0] * n
        cnt = [0] * n
        for i, x in enumerate(nums):
            dp[i] = 1
            cnt[i] = 1
            for j in range(i):
                if x > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        cnt[i] = cnt[j]  # 重置计数
                    elif dp[j] + 1 == dp[i]:
                        cnt[i] += cnt[j]
            if dp[i] > max_len:
                max_len = dp[i]
                ans = cnt[i]  # 重置计数
            elif dp[i] == max_len:
                ans += cnt[i]
        return ans

test = Solution()
print(test.findNumber0fLIS([1,3,5,4,7]))