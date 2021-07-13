from typing import List
import heapq


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if not buildings:
            return []
        h = []
        for left, right, height in buildings:
            h.append([left, -height, -right])

        ans = []
        heapq.heapify(h)
        now_point = heapq.heappop(h)


        while h:
            next_point = heapq.heappop(h)
            now_left, now_height, now_right = now_point[0], -now_point[1], -now_point[2]
            next_left, next_height, next_right = next_point[0], -next_point[1], -next_point[2]
            # 覆盖
            if now_left <= next_left and now_height >= next_height and now_right >= next_right:
                continue
            # 重合且同一高度
            elif now_right >= next_left and now_height == next_height:
                now_point[2] = -max(now_right, next_right)
            # 相邻
            elif now_right == next_left:
                ans.append([now_left, now_height])
                now_point = next_point
            # 错开
            elif now_right < next_left:
                ans.append([now_left, now_height])
                ans.append([now_right, 0])
                now_point = next_point
            # 重合，凸形
            elif now_height < next_height and now_right >= next_right:
                ans.append([now_left, now_height])
                heapq.heappush(h, [next_right, -now_height, -now_right])
                now_point = next_point
            # 重合，高，右边突出
            elif now_right >= next_left and now_height < next_height:
                ans.append([now_left, now_height])
                now_point = next_point
            # 重合，低，右边突出
            elif now_right >= next_left and now_height > next_height:
                heapq.heappush(h, [now_right, -next_height, -next_right])

        now_left, now_height, now_right = now_point[0], -now_point[1], -now_point[2]
        ans.append([now_left, now_height])
        ans.append([now_right, 0])
        return ans

test = Solution()
print(test.getSkyline([[1,2,1],[1,2,2],[1,2,3]]))


