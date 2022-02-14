class Solution:
    def balancedStringSplit(self, s: str) -> int:
        t = 0
        n = len(s)
        p = 0
        ans = 0
        while p < n:
            if s[p] == 'L':
                t += 1
            else:
                t -= 1
            if t == 0:
                ans += 1
            p += 1
        return ans

test = Solution()
print(test.balancedStringSplit("RLLLLRRRLR"))