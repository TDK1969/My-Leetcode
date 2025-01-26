"""
日期: 2024-09-27
题目: 每种字符至少取 K 个
链接: https://leetcode.cn/problems/take-k-of-each-character-from-left-and-right/
"""

from typing import *
from collections import *
from leetcode_utils import *
import bisect
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        c = Counter(s)
        if c["a"] < k or c["b"] < k or c["c"] < k:
            return -1
        n = len(s)
        pre_a = [0]
        pre_b = [0]
        pre_c = [0]
        for i in range(n):
            if s[i] == "a":
                pre_a.append(pre_a[-1] + 1)
                pre_b.append(pre_b[-1])
                pre_c.append(pre_c[-1])
            elif s[i] == "b":
                pre_a.append(pre_a[-1])
                pre_b.append(pre_b[-1] + 1)
                pre_c.append(pre_c[-1])
            elif s[i] == "c":
                pre_a.append(pre_a[-1])
                pre_b.append(pre_b[-1])
                pre_c.append(pre_c[-1] + 1)

        tail_a = [0]
        tail_b = [0]
        tail_c = [0]
        for i in range(n - 1, -1, -1):
            if s[i] == "a":
                tail_a.append(tail_a[-1] + 1)
                tail_b.append(tail_b[-1])
                tail_c.append(tail_c[-1])
            elif s[i] == "b":
                tail_a.append(tail_a[-1])
                tail_b.append(tail_b[-1] + 1)
                tail_c.append(tail_c[-1])
            elif s[i] == "c":
                tail_a.append(tail_a[-1])
                tail_b.append(tail_b[-1])
                tail_c.append(tail_c[-1] + 1)
        
        ans = n
        for i in range(n):
            left_a = k - pre_a[i]
            left_b = k - pre_b[i]
            left_c = k - pre_c[i]

            
            r_a = bisect.bisect_left(tail_a, left_a)
            r_b = bisect.bisect_left(tail_b, left_b)
            r_c = bisect.bisect_left(tail_c, left_c)

            ans = min(ans, i + max(r_a, r_b, r_c))
        return ans
                

print(Solution().takeCharacters("a",1))

"""
--TESTCASE BEGIN--
TestCase 0: "aabaaaacaabc",2
TestCase 1: "a",1
--TESTCASE END--
""" 
