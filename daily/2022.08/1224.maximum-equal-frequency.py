"""
日期: 2022-08-18
题目: 最大相等频率
链接: https://leetcode-cn.com/problems/maximum-equal-frequency/
"""

from typing import *
from collections import *
class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        max_cnt = 0
        one_cnt = set()
        num_cnt = dict()
        ans = 1

        for i in range(len(nums)):
            l = i + 1
            if nums[i] not in num_cnt:
                one_cnt.add(nums[i])
                num_cnt[nums[i]] = 0
            else:
                if nums[i] in one_cnt:
                    one_cnt.remove(nums[i])
            num_cnt[nums[i]] += 1
            max_cnt = max(max_cnt, num_cnt[nums[i]])
            if len(num_cnt) == 1:
                ans = max(ans, l) 
            else:
                if one_cnt and i == (len(num_cnt) - 1) * max_cnt:
                    ans = max(ans, l)
                if one_cnt and i == len(num_cnt) * max_cnt:
                    ans = max(ans, l)
                if i == len(num_cnt) * (max_cnt - 1):
                    ans = max(ans, l)
        return ans

test = Solution()
print(test.maxEqualFreq(nums = [1,1,1,2,2,2]))


