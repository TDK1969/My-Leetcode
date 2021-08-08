class Solution:
    def tribonacci(self, n: int) -> int:
        tri = [0 for _ in range(38)]
        tri[0] = 0
        tri[1] = 1
        tri[2] = 1
        for i in range(3, 38):
            tri[i] = tri[i - 3] + tri[i - 2] + tri[i - 1]
        return tri[n]
test = Solution()
print(test.tribonacci(25))