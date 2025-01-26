from typing import List

def solution(nums: List[int], n: int) -> int:
    if n == 1:
        return nums[0]
    dp = [[-float("inf"), -float("inf")] for _ in range(n + 1)]
    dp[0][0] = dp[0][1] = 0
    dp[1][0] = nums[0]
    dp[1][1] = -nums[0]
    dp[2][0] = nums[0] + nums[1]
    dp[2][1] = -nums[0] - nums[1]
    for i in range(2, n):
        dp[i + 1][0] = max(dp[i][0], dp[i][1]) + nums[i]
        dp[i + 1][1] = max(
            dp[i][0] - nums[i - 1] * 2,
            dp[i][1] + nums[i - 1] * 2
        ) - nums[i]
    
    return max(dp[-1][0], dp[-1][1])

print(solution([1, -2, 3, -4, 5], 5))
