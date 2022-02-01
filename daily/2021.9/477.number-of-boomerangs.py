from typing import List
from collections import defaultdict

class Solution:
    def number0fBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for point in points:
            distances = defaultdict(int)
            for next_point in points:
                d = (point[0] - next_point[0]) ** 2 + (point[1] - next_point[1]) ** 2
                distances[d] += 1
                ans += 2 * (distances[d] - 1)
        return ans

test = Solution()
print(test.number0fBoomerangs([[0,0],[1,0],[2,0]]))