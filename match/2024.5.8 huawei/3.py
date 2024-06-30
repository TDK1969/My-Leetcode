from typing import List
def solution(src: List[int]) -> List[int]:
    timeline = []
    n = len(src)
    for i in range(n):
        period, offset = src[i][0], src[i][1]
        k = offset
        while k < 512:
            timeline.append([k, i])
            k += period
    timeline.sort()

    min_len = 512
    ans_start = 0

    cnt = [0] * n
    left = right = 0
    while right < len(timeline):
        cnt[timeline[right][1]] += 1
        right += 1
        if all([x > 0 for x in cnt]) and left <= right:
            while cnt[timeline[left][1]] >= 2:
                cnt[timeline[left][1]] -= 1
                left += 1
        # 此时 [left, right]包含全部元素且left不可缩小

            if right == len(timeline):
                window_len = timeline[right - 1][0] - timeline[left][0]
            else:
                window_len = timeline[right][0] - timeline[left][0]
            if window_len < min_len:
                min_len = window_len
                ans_start = timeline[left][0]
    
    return [ans_start, min_len]


print(solution([[16, 7], [10, 5], [20, 4], [20, 16]]))


        



