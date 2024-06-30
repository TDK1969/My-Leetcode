from typing import List
def solution(n: int, s: str) -> List[int]:
    # dp[i][1]表示s[i]改为PDD的最后一位D时前i个字符串的最小总代价，dp[i][0]表示s[i]不参与
    if n < 3:
        return [0, 0]
    dp = [[[0, 0], [0, 0]] for _ in range(n)]
    # "P": 80  "D": 68 PDD = 216
    dp[2][1][0] = 1
    dp[2][1][1] = abs(80 - ord(s[0])) + abs(68 - ord(s[1])) + abs(68 - ord(s[2]))

    for i in range(3, n):
        if dp[i - 1][1][0] > dp[i - 1][0][0]:
            dp[i][0][0] = dp[i - 1][1][0]
            dp[i][0][1] = dp[i - 1][1][1]
        else:
            dp[i][0][0] = dp[i - 1][1][0]
            dp[i][0][1] = min(dp[i - 1][1][1], dp[i - 1][0][1])
        
        dp[i][1] = dp[i - 2][0].copy()
        dp[i][1][0] += 1
        dp[i][1][1] += abs(80 - ord(s[i - 2])) + abs(68 - ord(s[i - 1])) + abs(68 - ord(s[i]))
    
    if dp[-1][1][0] > dp[-1][0][0]:
        return dp[-1][1]
    else:
        return min(dp[-1][0], dp[-1][1])

print(solution(7, "ABCDEFG"))
