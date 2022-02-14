class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        if k == 0:
            return 0
        if k == 1:
            return 1
        F1 = 1
        F2 = 1

        while F2 <= k:
            F1, F2 = F2, F1 + F2
        # 贪心策略，每次都取小于k中最大的斐波那契数
        # 可以先打表，然后用二分进行优化
        return self.findMinFibonacciNumbers(k - F1) + 1

test = Solution()
print(test.findMinFibonacciNumbers(7))