class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        subsequence = set()
        letters = set(list(s))

        for letter in letters:
            front = s.index(letter)
            rear = len(s) - 1 - s[::-1].index(letter)
            for i in range(front + 1, rear):
                subsequence.add(letter + s[i] + letter)

        return len(subsequence)

test = Solution()
print(test.countPalindromicSubsequence("aabca"))
