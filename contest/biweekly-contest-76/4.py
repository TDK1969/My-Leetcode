from typing import List
from collections import defaultdict
class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        e = defaultdict(set)
        group = dict()

        for n1, n2 in edges:
            e[n1].add(n2)
            e[n2].add(n1)


