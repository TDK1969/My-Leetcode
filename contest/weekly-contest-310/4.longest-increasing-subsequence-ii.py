"""
题目: 最长递增子序列 II
链接: https://leetcode-cn.com/problems/longest-increasing-subsequence-ii/
"""

from typing import *
from collections import *
class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        stack = []
        n = len(nums)
        ans = 0
        for num in nums[::-1]:
            if not stack:
                stack.append([num, 1])
            else:
                if num < stack[-1][0]:
                    stack.append([num, 1])
                else:
                    while stack and stack[-1][0] < num:
                        t, l = stack.pop()
                        ans = max(ans, l)
                        if stack and stack[-1][0] - t <= k:
                            stack[-1][1] += l
                    if not stack or stack[-1][0] != num:
                        stack.append([num, 1])
        while stack:
            t, l = stack.pop()
            ans = max(ans, l)
            if stack and stack[-1][0] - t <= k:
                stack[-1][1] = l + 1
        return ans

test = Solution()
print(test.lengthOfLIS(nums = [4,2,1,4,3,4,5,8,15], k = 3))
                        