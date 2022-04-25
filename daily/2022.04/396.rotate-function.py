"""
日期: 2022-04-22
题目: 旋转函数
链接: https://leetcode-cn.com/problems/rotate-function/
"""
from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        nums_sum = sum(nums)
        temp_f = 0
        for index, value in enumerate(nums):
            temp_f += index * value
        
        max_f = temp_f

        # key: 在O(1)时间内进行转移
        for i in range(1, n):
            temp_f = temp_f + nums_sum - n * nums[- i]
            max_f = max(max_f, temp_f)
        
        return max_f