from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # 将word[left]到word[right-1]的单词组合成一个左右对齐的行
        def process(left, right):
            # 结尾行，向后补齐空格
            if right == n:
                res = ' '.join(words[left:right])
                res += ' ' * (maxWidth - len(res))
                return res
            spaces = right - left - 1
            # 单独单词构成的行，向后补齐空格
            if not spaces:
                return words[left] + ' ' * (maxWidth - len(words[left]))
            cur = sum(len(w) for w in words[left:right]) + spaces
            # 统计每个空隙间的空格数
            each = [1] * spaces
            j = 0
            while cur < maxWidth:
                # 根据题意优先补左边，所以从0开始
                each[j] += 1
                j += 1
                if j == spaces:
                    j = 0
                cur += 1
            j = 0
            res = ''
            # 根据每个间隙的空格数构建该行字符串
            while left < right:
                res += words[left]
                if left < right - 1:
                    res += ' ' * each[j]
                    j += 1
                left += 1
            return res

        n = len(words)
        idx = i = 0
        ans = []
        while idx < n:
            i = idx
            curLen = len(words[idx])
            idx += 1
            # 统计哪些单词组成一行
            while idx < n and curLen < maxWidth:
                # 单词之间需要空格
                curLen += 1
                curLen += len(words[idx])
                idx += 1
            if curLen > maxWidth:
                idx -= 1
                curLen -= len(words[idx]) + 1
            ans.append(process(i, idx))
        return ans

test = Solution()
print(test.fullJustify(words = ["What","must","be","acknowledgment","shall","be"],maxWidth = 16))





