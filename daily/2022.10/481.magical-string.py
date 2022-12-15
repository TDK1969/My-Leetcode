"""
日期: 2022-10-31
题目: 神奇字符串
链接: https://leetcode-cn.com/problems/magical-string/
"""

from typing import *
from collections import *
class Solution:
    def magicalString(self, n: int) -> int:
        s = [0 for _ in range(n + 3)]
        ans = 1
        flag = 1
        s[0] = 1
        s[1] = 2
        s[2] = 2
        left = 2
        right = 3

        while right < n:
            if s[left] == 1:
                s[right] = flag
                right += 1
                if flag == 1:
                    ans += 1
            if s[left] == 2:
                s[right] = flag
                if flag == 1:
                    ans += 1
                right += 1
                
                s[right] = flag
                if flag == 1 and right < n:
                    ans += 1
                right += 1

            left += 1

            flag = flag % 2 + 1
        
        return ans

test = Solution()
print(test.magicalString(4))
        
        



