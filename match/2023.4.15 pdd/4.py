def solution(n: int, m: int, k: int) -> int:
    if k > n * m:
        return -1
    if k == n * m:
        return 0

    