"""
日期: 2023-06-27
题目: 删除一次得到子数组最大和
链接: https://leetcode-cn.com/problems/maximum-subarray-sum-with-one-deletion/
"""

from typing import *
from collections import *
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        pre_0 = arr[0]
        pre_1 = 0
        ans = arr[0]

        for i in range(1, n):
            pre_0, pre_1 = max(pre_0, 0) + arr[i], max(pre_0, pre_1 + arr[i])
            ans = max(ans, pre_0, pre_1)
        
        return ans
