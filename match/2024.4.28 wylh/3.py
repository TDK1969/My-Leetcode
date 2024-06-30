# 找到最优的m和n
# pi和老虎最多相差一天开始断食

def count(m: int, n: int, p: int, q: int) -> int:
    # m 食物 n 水 p老虎 q人
    ans = -1
    d = min(m // 3, n // 3)
    # d天后，会出现断食断饮
    m_left, n_left = m - d * 3, n - d * 3

    if m_left < 2 and n_left < 2 or m_left == 0 or n_left == 0:
        # 人和虎都没得吃
        ans = max(ans, d + min(p, q))
    if m_left >= 2 and n_left >= 1:
        # 只给老虎吃
        ans = max(ans, min(d + q, d + min(n_left, m_left // 2) + p))
    if m_left >= 1 and n_left >= 2:
        # 只给人吃
        ans = max(ans, min(d + min(m_left, n_left // 2) + q, d + p))
    return ans

n = 99
print(count(397-3 * n, n, 9, 5))

