from typing import List
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        a = []
        heapq.heapify(a)
        n = len(profits)
        projects = []
        for i in range(n):
            if capital[i] < profits[i]:
                projects.append((capital[i], profits[i]))
        projects.sort(reverse=True)

        while k:
            while projects and w >= projects[-1][0]:
                heapq.heappush(a, -projects[-1][1])
                projects.pop()
            if not a:
                return w
            w += -heapq.heappop(a)


            k -= 1

        return w

test = Solution()
print(test.findMaximizedCapital(k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]))


        