"""
日期: 2022-04-28
题目: 按奇偶排序数组
链接: https://leetcode-cn.com/problems/sort-array-by-parity/
"""
from typing import List


class Solution:
    def sortArrayByParity1(self, nums: List[int]) -> List[int]:
        odd, even  = [], []
        for num in nums:
            if num & 1:
                odd.append(num)
            else:
                even.append(num)
        return even + odd
    def sortArrayByParity2(self, nums: List[int]) -> List[int]:
        p, q = 0, len(nums) - 1
        while p < q:
            while nums[p] & 1 == 0 and p < q:
                p += 1
            while nums[q] & 1 == 1 and p < q:
                q -= 1
            if p < q:
                nums[p], nums[q] = nums[q], nums[p]
        return nums
        