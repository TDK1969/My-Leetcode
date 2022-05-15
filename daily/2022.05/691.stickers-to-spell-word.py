"""
日期: 2022-05-14
题目: 贴纸拼词
链接: https://leetcode-cn.com/problems/stickers-to-spell-word/
"""

from typing import *
from collections import *
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        n = len(target)
        dp = [float("inf") for _ in range(1 << n)]
        dp[0] = 0

        for i in range(0, 1 << n):
            if dp[i] == float("inf"):
                continue
            
            for s in stickers:
                state = i
                for alpha in s:
                    for index in range(n):
                        if target[index] == alpha and (state & 1 << index) == 0:
                            state |= 1 << index
                            break
                dp[state] = min(dp[state], dp[i] + 1)
        
        return dp[-1] if dp[-1] != float("inf") else -1
        
test = Solution()
print(test.minStickers(stickers = ["with","example","science"], target = "thehat"))