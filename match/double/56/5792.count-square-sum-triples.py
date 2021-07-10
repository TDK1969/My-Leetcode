class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                cc = a ** 2 + b ** 2
                c = int(cc ** 0.5)
                if c ** 2 == cc and 1 <= c <= n:
                    count += 1
        return count

test = Solution()
print(test.countTriples(10))