"""
日期: 2024-03-12
题目: 寻找重复数
链接: https://leetcode-cn.com/problems/find-the-duplicate-number/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow, fast = nums[slow], nums[nums[fast]]
        
        slow = 0
        while slow != fast:
            slow, fast = nums[slow], nums[fast]
        
        return slow
        
print(Solution().findDuplicate([1,3,4,2,2]))            


"""
--TESTCASE BEGIN--
TestCase 0: [1,3,4,2,2]
TestCase 1: [3,1,3,4,2]
TestCase 2: [3,3,3,3,3]
--TESTCASE END--
""" 
