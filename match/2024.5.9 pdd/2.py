def solution(s: str) -> int:
    n = len(s)
    first_0 = -1
    last_1 = n
    ori_sum = 0

    for i in range(n):
        
