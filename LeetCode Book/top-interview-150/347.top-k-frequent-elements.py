"""
日期: 2024-03-12
题目: 前 K 个高频元素
链接: https://leetcode-cn.com/problems/top-k-frequent-elements/
"""

from typing import *
from collections import *
from leetcode_utils import *
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)

        bucket = [[] for _ in range((10 ** 5) + 5)]
        for num, cnt in c.items():
            bucket[cnt].append(num)
        ans = []
        i = (10 ** 5) + 4
        while i >= 0 and len(ans) < k:
            for num in bucket[i]:
                ans.append(num)
            i -= 1
        return ans

    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        h = []
        heapq.heapify(h)

        c = Counter(nums)

        for num in c.keys():
            if len(h) < k:
                heapq.heappush(h, (c[num], num))
            else:
                cnt, temp = heapq.heappop(h)
                if cnt > c[num]:
                    heapq.heappush(h, (cnt, temp))
                else:
                    heapq.heappush(h, (c[num], num))
        return [k[1] for k in h]
    

print(Solution().topKFrequent([1,1,1,2,2,3],2))

"""
--TESTCASE BEGIN--
TestCase 0: [1,1,1,2,2,3],2
TestCase 1: [1],1
--TESTCASE END--
""" 
