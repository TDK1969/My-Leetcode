"""
日期: 2023-02-15
题目: 检查「好数组」
链接: https://leetcode-cn.com/problems/check-if-it-is-a-good-array/
"""

from typing import *
from collections import *
import math
class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        # 求整个数组的最大公约数,如果为1,则说明数组中存在互质的数
        for i in range(1, len(nums)):
            nums[i] = math.gcd(nums[i], nums[i - 1])
            if nums[i] == 1:
                return True
        return nums[0] == 1


