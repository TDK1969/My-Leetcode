import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [2, 3, 5]
        ugly = [1]
        visited = [1]

        for i in range(1, n + 1):
            min_ugly = heapq.heappop(ugly)
            if i == n:
                return min_ugly
            for num in nums:
                new_ugly = min_ugly * num
                if new_ugly not in visited:
                    visited.append(new_ugly)
                    heapq.heappush(ugly, new_ugly)
        
        return -1
