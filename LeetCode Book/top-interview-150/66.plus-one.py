"""
日期: 2024-03-09
题目: 加一
链接: https://leetcode-cn.com/problems/plus-one/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = []
        k = 1
        for digit in digits[::-1]:
            temp, k = (digit + k) % 10, (digit + k) // 10
            ans.append(temp)
        if k:
            ans.append(1)
        return ans[::-1]

print(Solution().plusOne([9,9]))

"""
--TESTCASE BEGIN--
TestCase 0: [1,2,3]
TestCase 1: [4,3,2,1]
TestCase 2: [9]
--TESTCASE END--
""" 
