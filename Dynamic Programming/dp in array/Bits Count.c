#include <stdlib.h>

int* countBits(int num, int* returnSize)
{
    int *one_bits = (int *)malloc(sizeof(int) * (num + 1));
    *returnSize = num + 1;
    int level = 1;

    one_bits[0] = 0;

    for (int i = 1; i <= num; i++) {
        if (i == level) {
            one_bits[i] = 1;
            level *= 2;
        } else {
            one_bits[i] = one_bits[i - level / 2] + 1;
        }
    }
    return one_bits;
}

int *countbits2(int num, int *returnSize)
{
    int *one_bits = (int *)malloc(sizeof(int) * (num + 1));
    *returnSize = num + 1;
    one_bits[0] = 0;

    for (int i = 1; i <= num; i++){
        if (i & 1) {
            one_bits[i] = one_bits[i - 1] + 1;
        } else {
            one_bits[i] = one_bits[i / 2];
        }
    }

    return one_bits;
}