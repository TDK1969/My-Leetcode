
# If you need to import additional packages or classes, please import here.
import sys
def func():

    # please define the python3 input here. For example: a,b = map(int, input().strip().split())
    # please finish the function body here.
    # please define the python3 output here. For example: print().
    msg = sys.stdin.readlines()
    a = [0] * 32
    for s in msg:
        if s[-1] == "\n":
            s = s[:-1]
        s = s.split(" ")
        dst = int(s[1][1:])
        if s[0] == "PRINT":
            print(a[dst])
        elif s[0] == "MOV":
            src = s[2]
            if src[0] == "a":
                v = a[int(src[1:])]
            else:
                v = int(src)
            a[dst] = v
        else:
            src0, src1 = s[2], s[3]
            if src0[0] == "a":
                v0 = a[int(src0[1:])]
            else:
                v0 = int(src0)
            if src1[0] == "a":
                v1 = a[int(src1[1:])]
            else:
                v1 = int(src1)
            
            if s[0] == "ADD":
                a[dst] = v0 + v1
            elif s[0] == "SUB":
                a[dst] = v0 - v1
            elif s[0] == "MUL":
                a[dst] = v0 * v1
            elif s[0] == "DIV":
                a[dst] = v0 // v1
            
        

if __name__ == "__main__":
    func()
