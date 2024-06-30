"""
日期: 2024-06-24
题目: 下一个更大元素 II
链接: https://leetcode.cn/problems/next-greater-element-ii/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        visited = set()
        s = []
        n = len(nums)
        ans = [-1 for _ in range(n)]
        nnums = nums + nums
        for i, num in enumerate(nnums):
            ii = i % n
            
            while s and s[-1][0] < num:
                _, pre_i = s.pop()
                visited.remove(pre_i)
                if ans[pre_i] == -1:
                    ans[pre_i] = num
            s.append((num, ii))

            if ii in visited:
                break
            visited.add(ii)
        return ans

print(Solution().nextGreaterElements([1,1,1,1,1]))

            

"""
--TESTCASE BEGIN--
TestCase 0: [1,2,1]
TestCase 1: [1,2,3,4,3]
--TESTCASE END--
""" 
