"""
日期: 2024-01-19
题目: 只出现一次的数字 II
链接: https://leetcode-cn.com/problems/single-number-ii/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            t = 0
            for num in nums:
                t += (num >> i) & 1
            ans |= (t % 3) << i
        if ans >= 2 ** 31:
            return ans - 2 ** 32
        return ans

print(Solution().singleNumber([-401451,-177656,-2147483646,-473874,-814645,-2147483646,-852036,-457533,-401451,-473874,-401451,-216555,-917279,-457533,-852036,-457533,-177656,-2147483646,-177656,-917279,-473874,-852036,-917279,-216555,-814645,2147483645,-2147483648,2147483645,-814645,2147483645,-216555]))
"""
--TESTCASE BEGIN--
TestCase 0: [2,2,3,2]
TestCase 1: [0,1,0,1,0,1,99]
--TESTCASE END--
""" 
