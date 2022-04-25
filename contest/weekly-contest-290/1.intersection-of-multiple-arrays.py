"""
题目: 多个数组求交集
链接: https://leetcode-cn.com/problems/intersection-of-multiple-arrays/
"""
from typing import List
from collections import Counter
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        count = Counter()
        n = nums
        for num in nums:
            count.update(num)
        
        ans = []
        times = count.most_common(1)
        if times[0][1] == len(nums):
            for val, _ in times:
                ans.append(val)
        return ans
