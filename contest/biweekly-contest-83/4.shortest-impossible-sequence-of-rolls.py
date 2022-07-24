"""
题目: 不可能得到的最短骰子序列
链接: https://leetcode-cn.com/problems/shortest-impossible-sequence-of-rolls/
"""

from typing import *
from collections import *
class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        n = len(rolls)
        s = set()
        index = 0
        ans = 1
        while True:
            cnt = 0
            a = 0
            s = set()
            for i in range(index, n):
                if rolls[i] in s:
                    continue
                else:
                    s.add(rolls[i])
                    cnt += 1
                    a = max(a, i)
                    if len(s) == k:
                        break
            if cnt < k:
                return ans
            index = a + 1
            ans += 1

test = Solution()
print(test.shortestSequence(rolls = [4,2,1,2,3,3,2,4,1], k = 4))

