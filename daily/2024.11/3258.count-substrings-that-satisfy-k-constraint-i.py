"""
日期: 2024-11-12
题目: 统计满足 K 约束的子字符串数量 I
链接: https://leetcode.cn/problems/count-substrings-that-satisfy-k-constraint-i/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        ans = 0
        left = right = 0
        n = len(s)
        cnt0 = cnt1 = 0

        while right < n:
            if s[right] == "1":
                cnt1 += 1
            else:
                cnt0 += 1
            while cnt0 > k and cnt1 > k:
                if s[left] == "1":
                    cnt1 -= 1
                else:
                    cnt0 -= 1
                left += 1
            ans += right - left + 1
            right += 1
        
        return ans

print(Solution().countKConstraintSubstrings("1010101",2))    

"""
--TESTCASE BEGIN--
TestCase 0: "10101",1
TestCase 1: "1010101",2
TestCase 2: "11111",1
--TESTCASE END--
""" 
