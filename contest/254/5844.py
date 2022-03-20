class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        n = 2**p - 1

        def quick_algorithm(a, b, c):
            a = a % c
            ans = 1
            while b != 0:
                if b & 1:
                    ans = (ans * a) % c
                b >>= 1
                a = (a * a) % c
            return ans
        return (n * quick_algorithm(n - 1, (n - 1) // 2, 10**9 + 7)) % (10**9 + 7)
test = Solution()
print(test.minNonZeroProduct(30))