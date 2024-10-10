"""
日期: 2024-10-10
题目: 优质数对的总数 I
链接: https://leetcode.cn/problems/find-the-number-of-good-pairs-i/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        c1 = Counter(nums1)
        c2 = Counter(nums2)

        ans = 0
        for i in c2.keys():
            for j in c1.keys():
                if j % (i * k) == 0:
                    ans += c2[i] * c1[j]
        return ans

print(Solution().numberOfPairs([1,2,4,12],[2,4],3))
"""
--TESTCASE BEGIN--
TestCase 0: [1,3,4],[1,3,4],1
TestCase 1: [1,2,4,12],[2,4],3
--TESTCASE END--
""" 
