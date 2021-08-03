from typing import List


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for num in range(left, right + 1):
            flag = False
            for r in ranges:
                if num in range(r[0], r[1] + 1):
                    flag = True
                    break
            if not flag:
                return False
        return True