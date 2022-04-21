"""
日期: 2022-04-21
题目: 山羊拉丁文
链接: https://leetcode-cn.com/problems/goat-latin/
"""
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split()
        yuan = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        tail = "maa"
        ans = []

        for word in words:
            if word[0] in yuan:
                goatWord = word
            else:
                goatWord = word[1:] + word[0]
            goatWord += tail
            tail += "a"
            ans.append(goatWord)
        
        return " ".join(ans)


            
