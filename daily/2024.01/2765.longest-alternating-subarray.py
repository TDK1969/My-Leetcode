"""
日期: 2024-01-23
题目: 最长交替子数组
链接: https://leetcode.cn/problems/longest-alternating-subarray/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        ans = -1
        t = 0
        flag = True # True表示应该+1，False表示应该-1
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                if flag:
                    if t == 0:
                        t = 2
                    else:
                        t += 1
                    flag = False
                else:
                    flag = False
                    t = 2
            elif nums[i] - nums[i - 1] == -1 and not flag:
                t += 1
                flag = True
            else:
                flag = True
                t = 0
            ans = max(ans, t)
        
        return ans if ans else -1
            
print(Solution().alternatingSubarray([64,65,64,65,64,65,66,65,66,65]))


"""
--TESTCASE BEGIN--
TestCase 0: [2,3,4,3,4]
TestCase 1: [4,5,6]
--TESTCASE END--
""" 
