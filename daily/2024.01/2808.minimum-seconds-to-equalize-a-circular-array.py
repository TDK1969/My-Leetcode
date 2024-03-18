"""
日期: 2024-01-30
题目: 使循环数组所有元素相等的最少秒数
链接: https://leetcode.cn/problems/minimum-seconds-to-equalize-a-circular-array/
"""

from typing import *
from collections import *
from leetcode_utils import *
from math import floor
class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        n = len(nums)
        mp = defaultdict(list)

        for i, num in enumerate(nums):
            mp[num].append(i)
        
        ans = float("inf")

        for pos in mp.values():
            k = floor((pos[0] + n - pos[-1]) // 2)
            for i in range(1, len(pos)):
                k = max(k, floor((pos[i] - pos[i - 1]) // 2))
            ans = min(ans, k)
        
        return ans

print(Solution().minimumSeconds([5,5,5,5]))    


"""
--TESTCASE BEGIN--
TestCase 0: [1,2,1,2]
TestCase 1: [2,1,3,3,2]
TestCase 2: [5,5,5,5]
--TESTCASE END--
""" 
