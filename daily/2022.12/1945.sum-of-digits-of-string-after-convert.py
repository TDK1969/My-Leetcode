"""
日期: 2022-12-15
题目: 字符串转化后的各位数字之和
链接: https://leetcode-cn.com/problems/sum-of-digits-of-string-after-convert/
"""

from typing import *
from collections import *
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        t = ""
        for alpha in s:
            t += str(ord(alpha) - 96)
        
        ans = int(t)
        for _ in range(k):
            temp = ans
            ans = 0
            while temp:
                ans += temp % 10
                temp = temp // 10
        
        return ans

test = Solution()
print(test.getLucky("leetcode", 2))

            
