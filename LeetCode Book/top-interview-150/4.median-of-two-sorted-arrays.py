"""
日期: 2022-07-14
题目: 寻找两个正序数组的中位数
链接: https://leetcode-cn.com/problems/median-of-two-sorted-arrays/
"""

from typing import *
from collections import *
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def get_k_th_num(start1: int, start2: int, k: int) -> int:
            if start1 == len(nums1):
                return nums2[start2 + k - 1]
            if start2 == len(nums2):
                return nums1[start1 + k - 1]
            if k == 1:
                return min(nums1[start1], nums2[start2])
            i = k // 2
            c1 = min(i, len(nums1) - start1)
            c2 = min(i, len(nums2) - start2)
            
            if nums1[start1 + c1 - 1] <= nums2[start2 + c2 - 1]:
                return get_k_th_num(start1 + c1, start2, k - c1)
            else:
                return get_k_th_num(start1, start2 + c2, k - c2)
        return (get_k_th_num(0, 0, (len(nums1) + len(nums2) + 1) // 2) + get_k_th_num(0, 0, (len(nums1) + len(nums2) + 2) // 2)) / 2

            
test = Solution()
print(test.findMedianSortedArrays(nums1 = [2, 3], nums2 = [1]))


