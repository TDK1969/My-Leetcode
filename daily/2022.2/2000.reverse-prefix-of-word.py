class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        return word if ch not in word else word[word.index(ch)::-1] + word[word.index(ch) + 1:]


test = Solution()
print(test.reversePrefix(word = "abcdefd", ch = "d"))