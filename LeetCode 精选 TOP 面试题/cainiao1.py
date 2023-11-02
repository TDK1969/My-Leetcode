
def func(left: int, right: int) -> int:
    # 给定区间[left, right],求区间内后置0最多的二进制数,并返回0的个数
    n = right.bit_length()
    ans = 0
    for i in range(1, n):
        if (right >> i) << i >= left:
            ans = i
    
    return ans 

print(func(11, 100))



# 示例用法

