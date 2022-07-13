class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        if m + n != len(s3):
            return False

        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0] = True
        # dp递推 dp[i][j]表示s1的前i个字符和s2的前j个字符能否交错表示
        for i in range(m + 1):
            for j in range(n + 1):
                if i != 0:
                    dp[i][j] |= dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                if j != 0:
                    dp[i][j] |= dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]

        return dp[-1][-1]

test = Solution()
print(test.isInterleave("aabcc", "dbbca", "aadbbcbcac"))