"""
题目: 和相等的子数组
链接: https://leetcode-cn.com/problems/find-subarrays-with-equal-sum/
"""

from tokenize import Triple
from typing import *
from collections import *

class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        cnt = defaultdict(int)
        n = len(nums)
        for i in range(n - 1):
            s = nums[i] + nums[i + 1]
            cnt[s] += 1
            if cnt[s] == 2:
                return True
        return False