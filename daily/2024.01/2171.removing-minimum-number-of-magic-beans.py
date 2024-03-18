"""
日期: 2024-01-18
题目: 拿出最少数目的魔法豆
链接: https://leetcode.cn/problems/removing-minimum-number-of-magic-beans/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        n = len(beans)
        ans = sum(beans)
        s = sum(beans)
        pre_count = [0]
        for bean in beans:
            pre_count.append(pre_count[-1] + bean)
        for i in range(n):
            # 0到i之前的减为0，i之后的减为beans[i] * 
            t = pre_count[i] + (s - pre_count[i + 1] - (n - i - 1) * beans[i])
            ans = min(ans, t)
        return ans
        
print(Solution().minimumRemoval([2,10,3,2]))

"""
--TESTCASE BEGIN--
TestCase 0: [4,1,6,5]
TestCase 1: [2,10,3,2]
--TESTCASE END--
""" 
