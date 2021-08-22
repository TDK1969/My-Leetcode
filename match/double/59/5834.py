class Solution:
    def minTimeToType(self, word: str) -> int:
        p = 0
        step = 0
        word = list(word)
        for letter in word:
            target = ord(letter) - ord('a')
            move = min(abs(target - p), 26 - abs(target - p))
            step += move + 1
            p = target
        return step

test = Solution()
print(test.minTimeToType("zjpc"))
