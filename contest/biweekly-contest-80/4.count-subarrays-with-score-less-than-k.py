"""
题目: 统计得分小于 K 的子数组数目
链接: https://leetcode-cn.com/problems/count-subarrays-with-score-less-than-k/
"""

from typing import *
from collections import *


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        n = len(nums)
        s = 0
        ans = 0

        while r < n:
            s += nums[r]
            t_score = s * (r - l + 1)
            if t_score < k:
                pass
            else:
                while s * (r - l + 1) >= k:
                    ans += r - l
                    s -= nums[l]
                    l += 1
            r += 1
                
        ans += (1 + r - l) * (r - l) // 2
        return ans

test = Solution()
print(test.countSubarrays(nums = [2,1,4,3,5], k = 10))
