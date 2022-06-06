"""
题目: 设计一个文本编辑器
链接: https://leetcode-cn.com/problems/design-a-text-editor/
"""

from typing import *
from collections import *

class TextEditor:

    def __init__(self):
        self.string = ""
        self.cursor = 0
        self.strlen = 0

    def addText(self, text: str) -> None:
        self.string = self.string[:self.cursor] + text + self.string[self.cursor:]
        self.cursor += len(text)
        self.strlen += len(text)

    def deleteText(self, k: int) -> int:
        if self.cursor > k:
            self.string = self.string[:self.cursor - k] + self.string[self.cursor:]
            self.cursor -= k
            self.strlen -= k
            return k
        elif self.cursor <= k:
            self.string = self.string[self.cursor:]
            temp = self.cursor
            self.cursor = 0
            self.strlen -= temp
            return temp
        

    def cursorLeft(self, k: int) -> str:
        self.cursor = max(0, self.cursor - k)
        return self.string[max(self.cursor - 10, 0):self.cursor]

    def cursorRight(self, k: int) -> str:
        self.cursor = min(self.strlen, self.cursor + k)
        return self.string[max(self.cursor - 10, 0):self.cursor]

test = TextEditor()
print(test.addText("leetcode"))
print(test.deleteText(4))
print(test.addText("practice"))
print(test.cursorRight(3))
print(test.cursorLeft(8))
print(test.deleteText(10))
print(test.addText("1234"))
print(test.cursorLeft(2))
print(test.cursorRight(6))

# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)