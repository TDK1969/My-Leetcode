"""
日期: 2022-07-14
题目: 三数之和
链接: https://leetcode-cn.com/problems/3sum/
"""

from typing import *
from collections import *
import bisect
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        if not nums or len(nums) < 3:
            return []
        # 对原始数组排序,保证选取的三个数之间的大小关系
        nums.sort()
        if nums[0] > 0:
            return []

        n = len(nums)
        for i in range(n):
            # 最外层,遍历三元组中第一位数为nums[i]的组合
            if nums[i] > 0:
                break
            # 避免重复,跳过
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 双指针进行第二层遍历,如果三数之和 > 0,则移动右指针变小;如果 < 0,则移动左指针变大
            # 关键三数之和 = 0时去重
            left = i + 1
            right = n - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left < n - 1 and nums[left] == nums[left + 1]:
                        left += 1
                    while right > i + 1 and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
        return ans

test = Solution()
print(test.threeSum(nums = [-1,0,1,2,-1,-4]))


        

