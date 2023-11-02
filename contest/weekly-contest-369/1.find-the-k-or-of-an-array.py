"""
题目: 找出数组中的 K-or 值
链接: https://leetcode-cn.com/problems/find-the-k-or-of-an-array/
"""

from typing import *
from collections import *
class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        bits = [0] * 32
        for num in nums:
            for i in range(32):
                if num & (1 << i):
                    bits[i] += 1
        
        ans = 0
        for index, value in enumerate(bits):
            if value >= k:
                ans += 1 << index
        return ans

print(Solution().findKOr([7,12,9,8,9,15], 4))