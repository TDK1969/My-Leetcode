"""
日期: 2023-10-19
题目: 同积元组
链接: https://leetcode-cn.com/problems/tuple-with-same-product/
"""

from typing import *
from collections import *
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        k = defaultdict(list)
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                k[nums[i] * nums[j]].append((i, j))
                
        ans = 0
        for i in k.keys():
            ans += 4 * (len(k[i]) * (len(k[i]) - 1))
        
        return ans

test = Solution()
print(test.tupleSameProduct([1,2,4,5,10]))
