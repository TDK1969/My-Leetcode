"""
题目: 最长优雅子数组
链接: https://leetcode-cn.com/problems/longest-nice-subarray/
"""

from typing import *
from collections import *

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        ans = 1
        left = 0
        right = 0
        d = [0 for _ in range(30)]

        n = len(nums)
        while right < n:
            t = nums[right]
            i = 0
            while t:
                if t & 1:
                    d[i] += 1  
                i += 1
                t = t >> 1
            
            while left < right and max(d) > 1:
                t = nums[left]
                i = 0
                while t:
                    if t & 1:
                        d[i] -= 1
                    i += 1
                    t = t >> 1
                left += 1
            ans = max(ans, right - left + 1)
            right += 1
        return ans
t = Solution()
print(t.longestNiceSubarray(nums = [536870399,890391654]))

            
            

                
