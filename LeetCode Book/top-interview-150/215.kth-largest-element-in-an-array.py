"""
日期: 2024-03-18
题目: 数组中的第K个最大元素
链接: https://leetcode-cn.com/problems/kth-largest-element-in-an-array/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        bucket = [0 for _ in range(20005)]
        for num in nums:
            bucket[num + 10000] += 1
        p = len(bucket) - 1
        while k and p >= 0:
            if bucket[p] > 0:
                if bucket[p] >= k:
                    return p - 10000
                else:
                    k -= bucket[p]
            p -= 1
        return -1


print(Solution().findKthLargest([3,2,1,5,5, 6,4],7))
"""
--TESTCASE BEGIN--
TestCase 0: [3,2,1,5,6,4],2
TestCase 1: [3,2,3,1,2,4,5,5,6],4
--TESTCASE END--
""" 
