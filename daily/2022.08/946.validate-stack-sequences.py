"""
日期: 2022-08-31
题目: 验证栈序列
链接: https://leetcode-cn.com/problems/validate-stack-sequences/
"""

from typing import *
from collections import *
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        j = 0
        n = len(pushed)

        while i < n:
            stack.append(pushed[i])
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
            i += 1
        return len(stack) == 0

test = Solution()
print(test.validateStackSequences(pushed = [1,2,3,4,5], popped = [4,5,3,2,1]))
