"""
题目: 将区间分为最少组数
链接: https://leetcode-cn.com/problems/divide-intervals-into-minimum-number-of-groups/
"""

from typing import *
from collections import *
class Solution:
    def partitionString(self, s: str) -> int:
        ans = 0
        left = right = 0
        visited = set()
        n = len(s)

        while right < n:
            if s[right] not in visited:
                visited.add(s[right])
                right += 1
            else:
                ans += 1
                visited.clear()
        return ans

test = Solution()
print(test.partitionString())