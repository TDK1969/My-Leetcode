from typing import List


class Solution1:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        ans = []
        line = [set() for i in range(10**5 + 5)]
        line_start = float("inf")
        line_end = float("-inf")
        for segment in segments:
            start, end, color = segment
            line_start = min(line_start, start)
            line_end = max(line_end, end)
            for i in range(start, end):
                line[i].add(color)
        temp_start = line_start
        temp_color = line[temp_start]
        for i in range(line_start + 1, line_end + 1):
            if not temp_color and line[i]:
                temp_start = i
                temp_color = line[i]
            if line[i] != temp_color:
                ans.append([temp_start, i, sum(temp_color)])
                temp_start = i
                temp_color = line[i]
        return ans

class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        ans = []
        lines = []
        for segment in segments:
            s_start, s_end, s_color = segment
            for i in range(len(lines)):
                line = lines[i]
                if s_start >= line[0] and s_end < line[1]:
                    new_color = line[2].copy()
                    new_color.add(s_color)

                    lines.append((s_start, s_end, new_color))
                    lines.append((line[0], s_start, line[2].copy()))
                    lines.append((s_end, line[1], line[2].copy()))


test = Solution()
print(test.splitPainting([[1,4,5],[1,4,7],[4,7,1],[4,7,11]]))

