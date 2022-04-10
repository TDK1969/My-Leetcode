"""
日期: 2022-04-10
题目: 唯一摩尔斯密码词
链接: https://leetcode-cn.com/problems/unique-morse-code-words/
"""
from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ans = set()

        for word in words:
            temp = ""
            for letter in word:
                temp += table[ord(letter) - 97]
            ans.add(temp)
        return len(ans)
