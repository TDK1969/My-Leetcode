"""
题目: 必须拿起的最小连续卡牌数
链接: https://leetcode-cn.com/problems/minimum-consecutive-cards-to-pick-up/
"""
from typing import List
from collections import defaultdict
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        card_index = {}
        min_diff = float("inf")
        for index, card in enumerate(cards):
            if card not in card_index:
                card_index[card] = index
            else:
                min_diff = min(index - card_index[card] + 1, min_diff)
                card_index[card] = index
        if min_diff == float("inf"):
            return -1
        return min_diff

            