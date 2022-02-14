class Solution:
    def countValidWords(self, sentence: str) -> int:
        words = sentence.split()
        ans = 0
        for word in words:
            n = len(word)
            if word.count('-') > 1:
                continue
            flag = True
            for index, bit in enumerate(word):
                if bit.isdigit():
                    flag = False
                    break
                if bit in ['!', '.', ','] and index != n - 1:
                    flag = False
                    break
                if bit == '-':
                    if index == 0 or index == n - 1:
                        flag = False
                        break
                    if not word[index - 1].isalpha() or not word[index + 1].isalpha():
                        flag = False
                        break
            if flag:
                ans += 1

        return ans

test = Solution()
print(test.countValidWords("!this  1-s b8d!"))



