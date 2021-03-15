/*int jump(int* nums, int numsSize)//超时
{
    int last = numsSize - 1;
    nums[last] = 0;
    for (int i = last - 1; i >= 0; i--) {
        int min = 0x3f3f3f;

        for (int j = 1; j <= nums[i]; j++) {
            if (i + j >= numsSize) {
                break;
            }
            if (nums[i + j] < min) {
                min = nums[i + j];
            }
        }

        nums[i] = min + 1;
    }

    return nums[0];
}
*/
#include <stdlib.h>
#include <string.h>
/*
typedef struct {超时
    int num;
    int step;
} node;
int jump(int* nums, int numsSize)
{
    node *queue = (node *)malloc(sizeof(node) * 10000000);
    int head = -1;
    int rear = -1;

    queue[++rear].num = 0;
    queue[rear].step = 0;
    head++;

    while (head <= rear) {
        node temp = queue[head++];
        if (temp.num == numsSize - 1) {
            return temp.step;
        }

        for (int i = 1; i <= nums[temp.num]; i++) {
            rear++;
            queue[rear].num = temp.num + i;
            queue[rear].step =  temp.step + 1;
        }
    }
    return -1;
}
*/

int jump(int* nums, int numsSize)//通过
{
    int *step = (int *)malloc(sizeof(int) * numsSize);
    memset(step, -1, sizeof(int) * numsSize);
    step[0] = 0;
    for (int i = 0; i < numsSize; i++) {
        for (int j = 1; j <= nums[i]; j++) {
            if (i + j >= numsSize) {
                break;
            }
            if (step[i + j] == -1) {
                step[i + j] = step[i] + 1;
            }
        }
    }
    return step[numsSize - 1];
}


int main()
{
    int nums[10] = {2,1,1,1,1};
    int res = jump(nums, 5);
    return 0;
}