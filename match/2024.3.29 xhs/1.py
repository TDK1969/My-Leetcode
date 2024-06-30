def solution(s: str) -> int:
    num = []
    op = []

    s = s.replace(" ", "")
    n = len(s)
    i = 0
    cur = 0
    while i < n:
        if s[i].isdigit():
            cur = cur * 10 + int(s[i])
        elif s[i] == "+" or s[i] == "-":
            num.append(cur)
            cur = 0
            op.append(s[i])
        else:
            # 处理乘除，在入栈时如果栈顶是+-需要先计算
            while op and (op[-1] == "+" and op[-1] == "-"):
                t1 = num.pop()
                t2 = num.pop()
                if op[-1] == "+":
                    num.append(t1 + t2)
                else:
                    num.append(t2 - t1)
                op.pop()
            num.append(cur)
            cur = 0
            op.append(s[i])
        i += 1

    num.append(cur)
    while op:
        t1 = num.pop()
        t2 = num.pop()
        if op[-1] == "+":
            num.append(t1 + t2)
        elif op[-1] == "-":
            num.append(t2 - t1)
        elif op[-1] == "*":
            num.append(t1 * t2)
        else:
            num.append(t2 // t1)
        op.pop()
    return num[0]
        

print(solution("9*-2"))



