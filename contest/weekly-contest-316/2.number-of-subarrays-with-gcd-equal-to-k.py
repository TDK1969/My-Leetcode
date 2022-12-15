"""
题目: 最大公因数等于 K 的子数组数目
链接: https://leetcode-cn.com/problems/number-of-subarrays-with-gcd-equal-to-k/
"""

from typing import *
from collections import *
class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        left = right = 0
        ans = 0
        n = len(nums)
        while right < n:
            if nums[right] % k == 0:
                right += 1
            else:
                
