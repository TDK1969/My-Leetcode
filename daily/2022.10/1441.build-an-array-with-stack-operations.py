"""
日期: 2022-10-15
题目: 用栈操作构建数组
链接: https://leetcode-cn.com/problems/build-an-array-with-stack-operations/
"""

from typing import *
from collections import *
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        i = 1
        j = 0
        ans = []
        while i <= n and j < len(target):
            ans.append("Push")
            if target[j] != i:
                ans.append("Pop")
            else:
                j += 1
            i += 1
        
        return ans

test = Solution()
print(test.buildArray(target = [1,2], n = 4))
        
            

                
            

        