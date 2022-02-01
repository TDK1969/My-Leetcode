class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        columnTitle = list(columnTitle)

        ans = 0
        for alpha in columnTitle:
            ans = ans * 26 + ord(alpha) - ord('A') + 1
        return ans

test = Solution()
print(test.titleToNumber("FXSHRXW"))
