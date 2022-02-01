class Solution:
    def removePalindromeSub(self, s: str) -> int:
        b, e = 0, len(s) - 1
        while b <= e:
            if s[b] != s[e]:
                return 2
            b += 1
            e -= 1
        return 1
