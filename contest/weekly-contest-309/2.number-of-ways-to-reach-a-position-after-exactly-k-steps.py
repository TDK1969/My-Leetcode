"""
题目: 恰好移动 k 步到达某一位置的方法数目
链接: https://leetcode-cn.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/
"""

from typing import *
from collections import *

class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        pre = [0 for _ in range(-500, 1505)]
        nxt = [0 for _ in range(-500, 1505)]
        s = startPos + 500
        e = endPos + 500
        pre[s - 1] = 1
        pre[s + 1] = 1
        t = k - 1
        MOD = 10 ** 9 + 7

        while t:
            nxt = [0 for _ in range(-500, 1505)]
            for i in range(len(pre)):
                if 0 <= i - 1 and pre[i]:
                    nxt[i - 1] = (pre[i] + nxt[i - 1]) % MOD
                if i + 1 < len(pre) and pre[i]:
                    nxt[i + 1] = (pre[i] + nxt[i + 1]) % MOD
            t -= 1
            pre = nxt
        
        return pre[e]

t = Solution()
print(t.numberOfWays(startPos = 1, endPos = 1000, k = 999))