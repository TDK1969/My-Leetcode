"""
日期: 2022-10-17
题目: 水果成篮
链接: https://leetcode-cn.com/problems/fruit-into-baskets/
"""

from typing import *
from collections import *
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = right = 0
        basket = defaultdict(int)
        ans = 0
        n = len(fruits)

        while right < n:
            if fruits[right] in basket or len(basket) < 2:
                basket[fruits[right]] += 1
                ans = max(ans, right - left + 1)
                right += 1
            else:
                while len(basket) == 2:
                    basket[fruits[left]] -= 1
                    if basket[fruits[left]] == 0:
                        basket.pop(fruits[left])
                    left += 1
        return ans


                
