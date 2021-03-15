#include <stdlib.h>
#include <string.h>
//可以改为动态数组
int rob(int* nums, int numsSize)
{
    int *maxMoney = (int *)malloc(sizeof(int) * numsSize);
    memset(maxMoney, 0, sizeof(int) * numsSize);

    for (int i = 0; i < numsSize; i++) {
        if (i == 0) {
            maxMoney[0] = nums[0];
        } else if (i == 1) {
            maxMoney[1] = max(nums[0], nums[1]);
        } else {
            maxMoney[i] = max(maxMoney[i - 2] + nums[i], maxMoney[i - 1]);
        }
    }
    return maxMoney[numsSize - 1];
}