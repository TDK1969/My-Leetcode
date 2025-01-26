"""
日期: 2024-10-29
题目: 生成不含相邻零的二进制字符串
链接: https://leetcode.cn/problems/generate-binary-strings-without-adjacent-zeros/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []
        q = deque()
        
        q.append("0")
        q.append("1")

        while q:
            cur = q.popleft()
            if len(cur) == n:
                ans.append(cur)
            elif cur[-1] == "1":
                q.append(cur + "1")
                q.append(cur + "0")
            else:
                q.append(cur + "1")
        return ans

print(Solution().validStrings(3))      

"""
--TESTCASE BEGIN--
TestCase 0: 3
TestCase 1: 1
--TESTCASE END--
""" 
