"""
题目: 合法分组的最少组数
链接: https://leetcode-cn.com/problems/minimum-number-of-groups-to-create-a-valid-assignment/
"""

from typing import *
from collections import *
class Solution:
    def minGroupsForValidAssignment(self, nums: List[int]) -> int:
        c = Counter(nums)
        group_cnt = list(c.values())
        ans1 = ans2 = 0
        min_group = min(group_cnt)
        for i in range(len(group_cnt)):
            ans1 += min((group_cnt[i] + min_group - 1) // min_group, group_cnt[i] // (min_group - 1) if group_cnt[i] % (min_group - 1) )
            ans2 += (group_cnt[i] + min_group) // (min_group + 1)
            
        return min(ans2, ans1)

test = Solution()
print(test.minGroupsForValidAssignment([1,1,3,3,1,1,2,2,3,1,3,2]))