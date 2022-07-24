"""
日期: 2022-07-23
题目: 重建序列
链接: https://leetcode-cn.com/problems/ur2n8P/
"""

from itertools import pairwise
from typing import *
from collections import *
class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        nxt = defaultdict(set)
        pre = defaultdict(set)

        for seq in sequences:
            for i in range(len(seq)):
                if i != 0:
                    pre[seq[i]].add(seq[i - 1])
                    pre[seq[i]] -= pre[seq[i - 1]]
                if i != len(seq) - 1:
                    nxt[seq[i]].add(seq[i + 1])
                    nxt[seq[i]] -= nxt[seq[i + 1]]
        
        for i, v in enumerate(nums[:-1]):
            if nums[i + 1] not in nxt[v] or v not in pre[nums[i + 1]]:
                return False
        return True

test = Solution()
print(test.sequenceReconstruction(nums = [4,1,5,2,6,3], sequences = [[5,2,6,3],[4,1,5,2]]))

