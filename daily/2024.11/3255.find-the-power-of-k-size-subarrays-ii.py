"""
日期: 2024-11-07
题目: 长度为 K 的子数组的能量值 II
链接: https://leetcode.cn/problems/find-the-power-of-k-size-subarrays-ii/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [-1 for _ in range(n - k + 1)]

        left = right = 0
        while right < n:
            if nums[right] == nums[left] + right - left:
                if right - left == k - 1:
                    # 满足子数组长度为k
                    ans[left] = nums[right]
                    left += 1
            else:
                left = right
            right += 1
        return ans
        

"""
--TESTCASE BEGIN--
TestCase 0: [1,2,3,4,3,2,5],3
TestCase 1: [2,2,2,2,2],4
TestCase 2: [3,2,3,2,3,2],2
--TESTCASE END--
""" 
