class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        a = [0 for i in range(n + 1)]
        a[1] = 1
        for i in range(2, n + 1):
            if i & 1:
                a[i] = a[(i - 1) // 2] + a[(i - 1) // 2 + 1]
            else:
                a[i] = a[i // 2]
        return max(a)
test = Solution()
print(test.getMaximumGenerated(7))