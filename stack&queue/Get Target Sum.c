#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int sum;
    int nownum;
} elem;

int total = 0;
int findTargetSumWays(int* nums, int numsSize, int S) 
{
    elem *stack = (elem *)malloc(sizeof(elem) * 1000000000);
    int top = -1;

    int count = 0;
    
    top++;
    stack[top].nownum = 0;
    stack[top].sum = 0;

    while (top != -1) {
        elem temp = stack[top--];

        if (temp.nownum == numsSize) {
            total++;
            if (temp.sum == S) {
                count++;
            }
            continue;
        } else {
            top++;
            stack[top].sum = temp.sum + nums[temp.nownum];
            stack[top].nownum = temp.nownum + 1;

            top++;
            stack[top].sum = temp.sum - nums[temp.nownum];
            stack[top].nownum = temp.nownum + 1;
        }   
    }

    return count;
}

int main ()
{
    int nums[10] = {5,2,2,7,3,7,9,0,2,3};
    int numc = 10;
    int sum = 9;

    printf("%d", findTargetSumWays(nums, numc, sum));
    return 0;
}