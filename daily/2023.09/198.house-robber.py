"""
日期: 2023-09-16
题目: 打家劫舍
链接: https://leetcode-cn.com/problems/house-robber/
"""

from typing import *
from collections import *
class Solution:
    def rob(self, nums: List[int]) -> int:
        # t1 表示偷当前房屋的最高金额,t2 表示不偷当前房屋的最高金额
        # 递推公式:
        # 偷当前房屋的最高金额=不偷上一件间房屋+当前房屋的金额
        # 不偷当前房屋的最高金额=max(偷/不偷上一件房屋的最高金额),因为偷不偷都行
        # t1, t2 = nums[0], 0
        # for i in range(1, len(nums)):
            # t1, t2 = t2 + nums[i], max(t1, t2)

        # return max(t1, t2) 

        t1 = t2 = 0
        for i in range(len(nums)):
            t1, t2 = t2, max(t2, t1 + nums[i])
        return t2
