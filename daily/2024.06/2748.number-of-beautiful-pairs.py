"""
日期: 2024-06-20
题目: 美丽下标对的数目
链接: https://leetcode.cn/problems/number-of-beautiful-pairs/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        gcd = {
            1: [1,2,3,4,5,6,7,8,9],
            2: [1,3,5,7,9],
            3: [1,2,4,5,7,8],
            4: [1,3,5,7,9],
            5: [1,2,3,4,6,7,8,9],
            6: [1,5,7],
            7: [1,2,3,4,5,6,8,9],
            8: [1,3,5,7,9],
            9: [1,2,4,5,7,8]
        }
        ans = 0
        counter = [0 for _ in range(10)]

        for num in nums:
            y = num % 10
            x = num
            while x >= 10:
                x = x // 10
            
            for k in gcd[y]:
                ans += counter[k]
            
            counter[x] += 1
        
        return ans

print(Solution().countBeautifulPairs([11,21,12]))
"""
--TESTCASE BEGIN--
TestCase 0: [2,5,1,4]
TestCase 1: [11,21,12]
--TESTCASE END--
""" 
