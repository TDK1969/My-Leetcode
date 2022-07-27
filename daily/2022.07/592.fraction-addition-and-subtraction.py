"""
日期: 2022-07-27
题目: 分数加减运算
链接: https://leetcode-cn.com/problems/fraction-addition-and-subtraction/
"""

from typing import *
from collections import *
class Solution:
    def fractionAddition(self, expression: str) -> str:
        def yuefen(a: int, b: int) -> Tuple[int, int]:
            if a == 0:
                return (0, 1)
            i, j = max(abs(a), b), min(abs(a), b)

            while i % j != 0:
                i, j = j, i % j
            return (a // j, b // j)
        
        op = "+"
        l, r = 0, 0
        n = len(expression)
        ans0, ans1 = 0, 1

        while l < n and r < n:
            if expression[r] == "+" or expression[r] == "-":
                if l != r:
                    t = expression[l:r].split("/")
                    p = int(t[0]) if op == "+" else -int(t[0])
                    q = int(t[1])
                    ans0, ans1 = ans0 * q + ans1 * p, ans1 * q
                    ans0, ans1 = yuefen(ans0, ans1)

                    #nums.append((int(t[0]) if op == "+" else -int(t[0]), int(t[1])))
                    op = expression[r]
                else:
                    op = expression[r]
                
                r += 1  
                l = r
            else:
                r += 1
        
        t = expression[l:r].split("/")
        p = int(t[0]) if op == "+" else -int(t[0])
        q = int(t[1])
        ans0, ans1 = ans0 * q + ans1 * p, ans1 * q
        ans0, ans1 = yuefen(ans0, ans1)
        
        return f"{ans0}/{ans1}"


test = Solution()
print(test.fractionAddition(expression = "1/2-1/2-1/3"))




