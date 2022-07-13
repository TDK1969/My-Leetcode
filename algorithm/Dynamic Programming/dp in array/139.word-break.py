class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: string
        :type wordDict: List[string]
        :rtype: bool
        """
        dp = [0] * (len(s) + 1)
        dp[0] = 1

        for i in range(1, len(s) + 1):
            for word in wordDict:
                if i >= len(word) and s[i - len(word):i] == word and dp[i - len(word)]:
                    dp[i] = 1

        if dp[-1]:
            return True
        else:
            return False
