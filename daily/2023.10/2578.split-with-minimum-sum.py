"""
日期: 2023-10-09
题目: 最小和分割
链接: https://leetcode-cn.com/problems/split-with-minimum-sum/
"""

from typing import *
from collections import *
class Solution:
    def splitNum(self, num: int) -> int:
        nums = list(str(num))
        nums.sort()
        return int("".join(nums[::2])) + int("".join(nums[1::2]))

test = Solution()
print(test.splitNum(4325))
        

