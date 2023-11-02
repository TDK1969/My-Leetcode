"""
日期: 2023-09-27
题目: 餐厅过滤器
链接: https://leetcode-cn.com/problems/filter-restaurants-by-vegan-friendly-price-and-distance/
"""

from typing import *
from collections import *
class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        ans = []
        for rid, rating, vegan, price, distance in restaurants:
            if (veganFriendly == 0 or vegan == 1) and price <= maxPrice and distance <= maxDistance:
                ans.append((rid, rating))
        ans.sort(key=lambda x:(x[1], x[0]), reverse=True)
        return [i[0] for i in ans]