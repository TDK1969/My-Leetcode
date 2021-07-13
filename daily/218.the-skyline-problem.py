from typing import List
import heapq


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if not buildings:
            return []








#test = Solution()
#test.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]])

a = [[2,1,1], [1,1,2], [1,2,1], [1,1,1]]
heapq.heapify(a)
print(a)

