"""
题目: 数组的最小相等和
链接: https://leetcode-cn.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/
"""

from typing import *
from collections import *
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        count1 = count2 = 0
        s1 = s2 = 0
        for num in nums1:
            if num == 0:
                count1 += 1
            s1 += num
        for num in nums2:
            if num == 0:
                count2 += 1
            s2 += num
        
        if count1 == 0 and count2 == 0:
            return s1 if s1 == s2 else -1
        if count1 == 0 and count2 != 0:
            return s1 if s1 >= s2 + count2 else -1
        if count2 == 0 and count1 != 0:
            return s2 if s2 >= s1 + count1 else -1
        if count1 != 0 and count2 != 0:
            return max(count1 + s1, count2 + s2)

print(Solution().minSum(nums1 = [3,2,0,1,0], nums2 = [6,5,0]))

        
