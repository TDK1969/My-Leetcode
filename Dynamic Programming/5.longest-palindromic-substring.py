class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        longest = 1
        begin = 0
        for i in range(n):
            dp[i][i] = True
        # 应该先枚举子串长度，因为根据dp[l][r] = dp[l + 1][r - 1]的关系，长串是否成立需要考虑短的串
        for length in range(2, n + 1):
            for l in range(n):
                r = l + length - 1
                if r >= n:
                    break
                if s[l] != s[r]:
                    dp[l][r] = False
                else:
                    if length <= 3:
                        dp[l][r] = True
                    else:
                        dp[l][r] = dp[l + 1][r - 1]
                if dp[l][r]:
                    if length > longest:
                        longest = length
                        begin = l
        return s[begin:begin + longest]

test = Solution()
print(test.longestPalindrome("aaaa"))