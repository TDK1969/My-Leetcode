"""
日期: 2022-07-14
题目: 合并两个有序数组
链接: https://leetcode-cn.com/problems/merge-sorted-array/
"""

from typing import *
from collections import *
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 要求原地,避免覆盖的情况,从后往前排
        i = m - 1
        j = n - 1
        k = m + n - 1

        while k >= 0:
            if i >= 0 and j >= 0:
                if nums1[i] > nums2[j]:
                    nums1[k] = nums1[i]
                    i -= 1
                    k -= 1
                else:
                    nums1[k] = nums2[j]
                    j -= 1
                    k -= 1
            elif j >= 0:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
            else:
                break
        print(nums1)

test = Solution()
print(test.merge(nums1 = [0,0,0], m = 0, nums2 = [1,2,3], n = 3))



