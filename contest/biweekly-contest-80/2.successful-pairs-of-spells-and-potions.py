"""
题目: 咒语和药水的成功对数
链接: https://leetcode-cn.com/problems/successful-pairs-of-spells-and-potions/
"""

from typing import *
from collections import *
import bisect

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(spells)
        m = len(potions)
        ans = [0 for _ in range(n)]
        for index, s in enumerate(spells):
            a = (success + s - 1) // s
            i = bisect.bisect_left(potions, a)
            ans[index] = m - i
        return ans

test = Solution()
print(test.successfulPairs(spells = [5,1,3], potions = [1,2,3,4,5], success = 7))