"""
日期: 2024-03-18
题目: 查找和最小的 K 对数字
链接: https://leetcode-cn.com/problems/find-k-pairs-with-smallest-sums/
"""

from typing import *
from collections import *
from leetcode_utils import *
import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        h = []
        heapq.heapify(h)

        n1, n2 = len(nums1), len(nums2)
        for i in range(min(n1, k)):
            heapq.heappush(h, (nums1[i] + nums2[0], i, 0))
        
        ans = []
        while h and len(ans) != k:
            _, i, j = heapq.heappop(h)
            ans.append((nums1[i], nums2[j]))
            if j + 1 < n2:
                heapq.heappush(h, (nums1[i] + nums2[j + 1], i, j + 1))
        
        return ans

print(Solution().kSmallestPairs([1,7,11],[2,4,6],3))       

"""
--TESTCASE BEGIN--
TestCase 0: [1,7,11],[2,4,6],3
TestCase 1: [1,1,2],[1,2,3],2
--TESTCASE END--
""" 
