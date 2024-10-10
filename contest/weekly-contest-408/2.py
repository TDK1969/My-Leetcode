import bisect
class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        # 质数的平方
        ans = 0
        limit = 10 ** 5
        primes = [True] * (limit + 1)
        p = 2
        while (p * p <= limit):
            if (primes[p] == True):
                for i in range(p * p, limit + 1, p):
                    primes[i] = False
            p += 1
        prime_numbers = [p for p in range(2, limit) if primes[p]]
        for prime in prime_numbers:
            if l <= prime * prime <= r:
                ans += 1
            elif prime * prime > r:
                break
        return r - l + 1 - ans

print(Solution().nonSpecialCount(4, 16))
