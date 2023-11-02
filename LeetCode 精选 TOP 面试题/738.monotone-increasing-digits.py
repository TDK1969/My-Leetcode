"""
日期: 2023-10-24
题目: 单调递增的数字
链接: https://leetcode-cn.com/problems/monotone-increasing-digits/
"""

from typing import *
from collections import *
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        if n == 0:
            return 0
        digits = list(map(int, list(str(n))))
        l = len(digits)
        ans = []
        for i in range(len(digits)):
            if not ans:
                ans.append(digits[i])
            else:
                if digits[i] >= ans[-1]:
                    ans.append(digits[i])
                else:
                    k = ans.pop() - 1
                    while ans and k < ans[-1]:
                        k = ans.pop() - 1
                    ans.append(k)
                    break
        ans = "".join([str(i) for i in ans])
        ans += (l - len(ans)) * "9"
        
        return int(ans)
    

test = Solution()
print(test.monotoneIncreasingDigits(332))