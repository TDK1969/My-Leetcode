class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def extend(left: int, right: int) -> int:
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1
    
        maxLen = 1
        ans = s[0]
        
        for i in range(n):
            t1 = extend(i, i)
            t2 = extend(i, i + 1)

            if t1 > maxLen:
                maxLen = t1
                ans = s[i - t1 // 2:i + 1 + t1 // 2]
            if t2 > maxLen:
                maxLen = t2
                ans = s[i + 1 - t2 // 2:i + 1 + t2 // 2]
        return ans

print(Solution().longestPalindrome("bbbbaababb"))