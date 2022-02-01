from typing import List
import heapq

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        p = [1]
        visited = {1}
        heapq.heapify(p)
        cnt = 0
        while 1:
            tmp = heapq.heappop(p)
            cnt += 1
            if cnt == n:
                return tmp
            for prime in primes:
                ugly = tmp * prime
                if ugly not in visited:
                    visited.add(ugly)
                    heapq.heappush(p, ugly)

class DpSolution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [1 for _ in range(n)]
        pointer = [0 for _ in range(len(primes))]

        for i in range(1, n):
            min_num = float("inf")
            for j in range(len(primes)):
                t = dp[pointer[j]] * primes[j]
                min_num = min(t, min_num)
            for j in range(len(primes)):
                if dp[pointer[j]] * primes[j] == min_num:
                    pointer[j] += 1
            dp[i] = min_num
        return dp[-1]

test = DpSolution()
print(test.nthSuperUglyNumber(12, [2,7,13,19]))
