class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        b, c = 1, 1
        mod = 10**9 + 7
        while n - 2:
            b, c = c, (b + c) % mod
            n -= 1
        return c
test = Solution()
print(test.fib(4))