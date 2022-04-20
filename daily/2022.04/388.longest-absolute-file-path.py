"""
日期: 2022-04-20
题目: 文件的最长绝对路径
链接: https://leetcode-cn.com/problems/longest-absolute-file-path/
"""
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        files = input.split('\n')
        maxLen = 0
        filePathLen = 0
        ans = ""

        fileLevel = []
        for i in files:
            level = i.count("\t")
            while len(fileLevel) > level:
                filePathLen -= fileLevel[-1]
                fileLevel.pop()
            i = i[level:]

            if "." in i:
                filePath = filePathLen + len(i) + level
                if filePath > maxLen:
                    maxLen = filePath
            else:
                fileLevel.append(len(i))
                filePathLen += len(i)
        return maxLen

test = Solution()
print(test.lengthLongestPath("file1.txt\nfile2.txt\nlongfile.txt"))
                    


                
        
