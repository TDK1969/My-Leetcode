"""
日期: 2024-05-22
题目: 找出输掉零场或一场比赛的玩家
链接: https://leetcode.cn/problems/find-players-with-zero-or-one-losses/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lost_cnt = dict()
        for w, l in matches:
            if w not in lost_cnt:
                lost_cnt[w] = 0
            if l not in lost_cnt:
                lost_cnt[l] = 0
            lost_cnt[l] += 1
        
        ans = [[], []]
        for player in lost_cnt.keys():
            if lost_cnt[player] == 0:
                ans[0].append(player)
            elif lost_cnt[player] == 1:
                ans[1].append(player)
        ans[0].sort()
        ans[1].sort()
    
        return ans

print(Solution().findWinners([[2,3],[1,3],[5,4],[6,4]]))

"""
--TESTCASE BEGIN--
TestCase 0: [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
TestCase 1: [[2,3],[1,3],[5,4],[6,4]]
--TESTCASE END--
""" 
