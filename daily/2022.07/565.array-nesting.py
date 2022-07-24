"""
日期: 2022-07-17
题目: 数组嵌套
链接: https://leetcode-cn.com/problems/array-nesting/
"""

from typing import *
from collections import *
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        count = [0 for _ in range(n)]
        ans = 0

        for num in nums:
            if count[num] == 0:
                length = 0
                while count[num] == 0:
                    length += 1
                    count[num] = 1
                    num = nums[num]
                    
                ans = max(ans, length)
        return ans

test = Solution()
print(test.arrayNesting([5,4,0,3,1,6,2]))
