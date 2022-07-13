class Solution:
    def numDecodings(self, s: str) -> int:
        # 有前导零直接返回0
        if s[0] == '0':
            return 0
        n = len(s)
        # dp数组为n+1，需要增加一位空字符
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        for j in range(2, n + 1):
            i = j - 1
            if s[i] != '0':
                dp[j] += dp[j - 1]
            if s[i - 1] == '1' or s[i - 1] == '2' and '0' <= s[i] <= '6':
                dp[j] += dp[j - 2]
        return dp[-1]
test = Solution()
print(test.numDecodings("226"))