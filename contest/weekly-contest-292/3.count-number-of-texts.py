"""
题目: 统计打字方案数
链接: https://leetcode-cn.com/problems/count-number-of-texts/
"""

from typing import *
from collections import *

class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        pressedKeys = "****" + pressedKeys
        n = len(pressedKeys)
        mod = (10 ** 9) + 7

        dp = [1 for _ in range(n)]
        

        for i in range(4, n):
            dp[i] = dp[i - 1]
            if pressedKeys[i] == pressedKeys[i - 1]:
                dp[i] = (dp[i] + dp[i - 2]) % mod
                if pressedKeys[i] == pressedKeys[i - 2]:
                    dp[i] = (dp[i] + dp[i - 3]) % mod
                    if pressedKeys[i] == pressedKeys[i - 3] and pressedKeys[i] in {"7", "9"}:
                        dp[i] = (dp[i] + dp[i - 4]) % mod
        return dp[-1]

test = Solution()
print(test.countTexts("22233"))