"""
日期: 2022-05-05
题目: 乘积小于 K 的子数组
链接: https://leetcode-cn.com/problems/subarray-product-less-than-k/
"""
from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = right = 0
        product = 1
        ans = 0
        n = len(nums)

        while right < n:
            product *= nums[right]
            if product < k:
                ans += right - left + 1
            else:
                while product >= k and left <= right:
                    product //= nums[left]
                    left += 1
                ans += right - left + 1
            right += 1
        return ans