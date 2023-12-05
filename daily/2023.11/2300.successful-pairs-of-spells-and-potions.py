'''
Descripttion: 
version: 
Author: TDK
Date: 2023-11-10 00:00:01
LastEditors: TDK
LastEditTime: 2023-11-10 10:47:48
'''
"""
日期: 2023-11-10
题目: 咒语和药水的成功对数
链接: https://leetcode-cn.com/problems/successful-pairs-of-spells-and-potions/
"""

from typing import *
from collections import *
import bisect
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans = []
        potions.sort()

        for spell in spells:
            k = (success + spell - 1) // spell
            index = bisect.bisect_left(potions, k)
            ans.append(len(potions) - index)
        return ans

print(Solution().successfulPairs(spells = [5,1,3], potions = [1,2,3,4,5], success = 7))
            


