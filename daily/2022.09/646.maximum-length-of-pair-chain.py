"""
日期: 2022-09-03
题目: 最长数对链
链接: https://leetcode-cn.com/problems/maximum-length-of-pair-chain/
"""

from typing import *
from collections import *
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x:x[1])
        ans = 1
        pre_j = pairs[0][1]

        for i, j in pairs[1:]:
            if i > pre_j:
                ans += 1
                pre_j = j
        return ans

test = Solution()
print(test.findLongestChain([[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[-5,3],[0,3]]))