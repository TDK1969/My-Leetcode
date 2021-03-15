#define  max(x,y)    ((x) > (y) ? (x) : (y))
#include <stdlib.h>
int rob(int* nums, int numsSize)
{
    if (numsSize == 0) {
        return 0;
    } else if (numsSize == 1) {
        return nums[0];
    } else if (numsSize == 2) {
        return max(nums[0], nums[1]);
    }

    int *maxMoney = (int *)malloc(sizeof(int) * numsSize);
    memset(maxMoney, 0, sizeof(int) * numsSize);
    
    for (int i = 0; i < numsSize - 1; i++) {
        if (i == 0) {
            maxMoney[0] = nums[0];
        } else if (i == 1) {
            maxMoney[1] = max(nums[0], nums[1]);
        } else {
            maxMoney[i] = max(maxMoney[i - 2] + nums[i], maxMoney[i - 1]);
        }
    }
    int dp1 = maxMoney[numsSize - 2];

    for (int i = 1; i < numsSize; i++) {
        if (i == 1) {
            maxMoney[1] = nums[1];
        } else if (i == 2) {
            maxMoney[2] = max(nums[1], nums[2]);
        } else {
            maxMoney[i] = max(maxMoney[i - 2] + nums[i], maxMoney[i - 1]);
        }
    }
    int dp2 = maxMoney[numsSize - 1];
    return max(dp1, dp2);
}