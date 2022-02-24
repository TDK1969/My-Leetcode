class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ans = ''
        i = 0
        j = len(s) - 1

        while i < len(s):
            if s[i].isalpha():
                while not s[j].isalpha():
                    j -= 1
                ans += s[j]
                j -= 1
            else:
                ans += s[i]
            i += 1
        return ans

test = Solution()
print(test.reverseOnlyLetters("a-bC-dEf-ghIj"))