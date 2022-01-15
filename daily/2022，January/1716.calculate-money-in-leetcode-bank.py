class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        fullWeek = n // 7
        ans += fullWeek * 28 +  fullWeek * (fullWeek - 1) // 2 * 7
        lastDays = n % 7
        ans += (1 + 2 * fullWeek + lastDays) * lastDays // 2
        return ans

test = Solution()
print(test.totalMoney(20))