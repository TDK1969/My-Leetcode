#include <stdbool.h>
#include <string.h>

bool canJump(int* nums, int numsSize)
{
    bool *visit = (bool *)malloc(sizeof(bool) * numsSize);
    memset(visit, false, sizeof(bool) * numsSize);
    visit[0] = true;
    for (int i = 0; i < numsSize; i++) {
        if (!visit[i]) {
            return false;
        }

        for (int j = 1; j <= nums[i]; j++) {
            if (i + j < numsSize) {
                visit[i + j] = true;
            }
        }
    }
    return true;
}