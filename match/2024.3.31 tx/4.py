from typing import List

def solution(n: int, k: int, nums: List[int]) -> int:
    xor = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    # xor[n][m] = nums[n:m]的异或
    for i in range(0, n):
        for j in range(i + 1, n + 1):
            if j == i + 1:
                xor[i][j] = nums[i]
            else:
                xor[i][j] = xor[i][j - 1] ^ nums[j - 1]
    
    # dp[i][j]表示nums[:i]分为j + 1段的分段异或最大和
    dp = [[0 for _ in range(k)] for _ in range(n + 1)]
    # 边界条件：nums[:i]分为1段
    for i in range(1, n + 1):
        dp[i][0] = xor[0][i]
    
    for j in range(1, k):
        for i in range(j + 1, n + 1):
            for p in range(1, i):
                dp[i][j] = max(dp[i][j], dp[i - p][j - 1] + xor[i - p][i])
    
    return dp[-1][-1]

print(solution(6, 2, [1,1,1,2,3,4]))



    