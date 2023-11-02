"""
日期: 2023-09-17
题目: 打家劫舍 II
链接: https://leetcode-cn.com/problems/house-robber-ii/
"""

from typing import *
from collections import *
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 不选最后一个房屋的最大金额
        t1 = t2 = 0
        for i in range(0, len(nums) - 1):
            t1, t2 = t2, max(t1 + nums[i])
        ans1 = t2

        # 不选第一个房屋的最大金额
        t1 = t2 = 0
        for i in range(1, len(nums)):
            t1, t2 = t2, max(t1 + nums[i])
        ans2 = t2

        # 以上两种办法不冲突，且能覆盖所有情况,返回两者最大值
        return max(ans1, ans2)