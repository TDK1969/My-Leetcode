class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def check(sub: str):
            set1 = set(sub)
            set2 = set(sub.upper())
            return len(set1) == 2 * len(set2)

        ans = ""
        n = len(s)

        for i in range(n):
            for j in range(i + 1, n + 1):
                if check(s[i:j]) and j - i > len(ans):
                    ans = s[i:j]

        return ans

test = Solution()
print(test.longestNiceSubstring("YazaAa"))
