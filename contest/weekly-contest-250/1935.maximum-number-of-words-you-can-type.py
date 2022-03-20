class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split()
        count = len(text)

        for word in text:
            for letter in brokenLetters:
                if letter in word:
                    count -= 1
                    break

        return count


