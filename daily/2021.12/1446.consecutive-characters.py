class Solution:
    def maxPower(self, s: str) -> int:
        maxLength = 1
        i = 0
        n = len(s)

        while i < n:
            tempLength = 1
            while i < n - 1:
                if s[i] == s[i + 1]:
                    tempLength += 1
                    i += 1
                else:
                    break
            i += 1
            maxLength = max(maxLength, tempLength)

        return maxLength


test = Solution()
print(test.maxPower("abbcccddddeeeeedcba"))


