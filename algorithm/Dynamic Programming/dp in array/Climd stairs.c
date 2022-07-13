//70. ÅÀÂ¥Ìİ
//·´Ïòì³²¨ÄÇÆõ
int climbStairs(int n)
{
    if (n == 1) {
        return 1;
    }

    int stairs[3];
    stairs[2] = 0;
    stairs[1] = 1;
    stairs[0] = 2;

    for (int i = 2; i < n; i++) {
        stairs[2] = stairs[1];
        stairs[1] = stairs[0];
        stairs[0] = stairs[2] + stairs[1];
    }

    return stairs[0];
}