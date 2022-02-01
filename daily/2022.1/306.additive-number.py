class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        