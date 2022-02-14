from typing import List


class Solution:
    def number0fArithmeticSlices(self, nums: List[int]) -> int:
        dp = [[0, 0] for _ in range(len(nums))]
        for i in range(2, len(nums)):
            total = dp[i - 1][0]
            end = dp[i - 1][1]
            dp[i][0] = total
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp[i][0] += end + 1
                dp[i][1] = end + 1
        return dp[-1][0]

    def number0fArithmeticSlicesBetterSpace(self, nums: List[int]) -> int:
        total = 0
        end = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                total += end + 1
                end += 1
            else:
                end = 0
        return total

test = Solution()
print(test.number0fArithmeticSlicesBetterSpace([1,2,3,4,6,8]))