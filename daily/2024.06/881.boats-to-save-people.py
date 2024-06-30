"""
日期: 2024-06-10
题目: 救生艇
链接: https://leetcode.cn/problems/boats-to-save-people/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        ans = 0
        n = len(people)
        left, right = 0, n - 1
        while left <= right:
            if left == right:
                ans += 1
                break
            if people[left] + people[right] <= limit:
                left += 1
            
            ans += 1
            right -= 1
        
        return ans

print(Solution().numRescueBoats([3,5,3,4],5))


"""
--TESTCASE BEGIN--
TestCase 0: [1,2],3
TestCase 1: [3,2,2,1],3
TestCase 2: [3,5,3,4],5
--TESTCASE END--
""" 
