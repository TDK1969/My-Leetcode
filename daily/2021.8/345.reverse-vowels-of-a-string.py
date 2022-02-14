class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        l = 0
        r = n - 1
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', '0', 'U'}
        # python修改字符串需要先将字符串变为列表
        s = list(s)
        while l < r:
            while l < n and s[l] not in vowels:
                l += 1
            while r >= 0 and s[r] not in vowels:
                r -= 1
            if l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        return "".join(s)

test = Solution()
print(test.reverseVowels("leetcode"))