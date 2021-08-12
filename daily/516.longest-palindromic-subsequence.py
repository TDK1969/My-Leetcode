class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        ans = 1  # 注意长度为1的情况，所以ans初值为1
        for i in range(n):
            dp[i][i] = 1
        for length in range(2, n + 1):
            for l in range(n):
                r = l + length - 1
                if r >= n:
                    break
                if s[l] != s[r]:
                    dp[l][r] = max(dp[l + 1][r], dp[l][r - 1])
                else:
                    dp[l][r] = max(dp[l + 1][r], dp[l][r - 1], dp[l + 1][r - 1] + 2)
                ans = max(ans, dp[l][r])
        return ans

test = Solution()
print(test.longestPalindromeSubseq("cbbd"))
